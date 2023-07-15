<?php
require_once 'database.php';
require_once 'Pengembalian.php';
$db = new MySQLDatabase();
$pengembalian = new Pengembalian($db);
$id=0;
$code_pengembalian=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['code_pengembalian'])){
            $code_pengembalian = $_GET['code_pengembalian'];
        }
        if($id>0){    
            $result = $pengembalian->get_by_id($id);
        }elseif($code_pengembalian>0){
            $result = $pengembalian->get_by_code_pengembalian($code_pengembalian);
        } else {
            $result = $pengembalian->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new pengembalian
        $pengembalian->code_pengembalian = $_POST['code_pengembalian'];
        $pengembalian->tanggal_kembali = $_POST['tanggal_kembali'];
        $pengembalian->batas_tgl_kembali = $_POST['batas_tgl_kembali'];
        $pengembalian->denda_per_hari = $_POST['denda_per_hari'];
        $pengembalian->jumlah_hari = $_POST['jumlah_hari'];
        $pengembalian->total_denda = $_POST['total_denda'];
        $pengembalian->kode_anggota = $_POST['kode_anggota'];
        $pengembalian->kode_buku = $_POST['kode_buku'];
        $pengembalian->kode_petugas = $_POST['kode_petugas'];
       
        $pengembalian->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pengembalian created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pengembalian not created.';
        }
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'PUT':
        // Update an existing data
        $_PUT = [];
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['code_pengembalian'])){
            $code_pengembalian = $_GET['code_pengembalian'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $pengembalian->code_pengembalian = $_PUT['code_pengembalian'];
        $pengembalian->tanggal_kembali = $_PUT['tanggal_kembali'];
        $pengembalian->batas_tgl_kembali = $_PUT['batas_tgl_kembali'];
        $pengembalian->denda_per_hari = $_PUT['denda_per_hari'];
        $pengembalian->jumlah_hari = $_PUT['jumlah_hari'];
        $pengembalian->total_denda = $_PUT['total_denda'];
        $pengembalian->kode_anggota = $_PUT['kode_anggota'];
        $pengembalian->kode_buku = $_PUT['kode_buku'];
        $pengembalian->kode_petugas = $_PUT['kode_petugas'];
        if($id>0){    
            $pengembalian->update($id);
        }elseif($code_pengembalian<>""){
            $pengembalian->update_by_code_pengembalian($code_pengembalian);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pengembalian updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pengembalian update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['code_pengembalian'])){
            $code_pengembalian = $_GET['code_pengembalian'];
        }
        if($id>0){    
            $pengembalian->delete($id);
        }elseif($code_pengembalian>0){
            $pengembalian->delete_by_code_pengembalian($code_pengembalian);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pengembalian deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pengembalian delete failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    default:
        header("HTTP/1.0 405 Method Not Allowed");
        break;
    }
$db->close()
?>