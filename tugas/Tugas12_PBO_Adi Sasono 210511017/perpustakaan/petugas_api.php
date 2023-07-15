<?php
require_once 'database.php';
require_once 'Petugas.php';
$db = new MySQLDatabase();
$petugas = new Petugas($db);
$id=0;
$code_petugas=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['code_petugas'])){
            $code_petugas = $_GET['code_petugas'];
        }
        if($id>0){    
            $result = $petugas->get_by_id($id);
        }elseif($code_petugas>0){
            $result = $petugas->get_by_code_petugas($code_petugas);
        } else {
            $result = $petugas->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new petugas
        $petugas->code_petugas = $_POST['code_petugas'];
        $petugas->nama = $_POST['nama'];
        $petugas->jk_petugas = $_POST['jk_petugas'];
        $petugas->jabatan = $_POST['jabatan'];
        $petugas->no_telepon = $_POST['no_telepon'];
        $petugas->alamat = $_POST['alamat'];
       
        $petugas->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Petugas created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Petugas not created.';
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
        if(isset($_GET['code_petugas'])){
            $code_petugas = $_GET['code_petugas'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $petugas->code_petugas = $_PUT['code_petugas'];
        $petugas->nama = $_PUT['nama'];
        $petugas->jk_petugas = $_PUT['jk_petugas'];
        $petugas->jabatan = $_PUT['jabatan'];
        $petugas->no_telepon = $_PUT['no_telepon'];
        $petugas->alamat = $_PUT['alamat'];
        if($id>0){    
            $petugas->update($id);
        }elseif($code_petugas<>""){
            $petugas->update_by_code_petugas($code_petugas);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Petugas updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Petugas update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['code_petugas'])){
            $code_petugas = $_GET['code_petugas'];
        }
        if($id>0){    
            $petugas->delete($id);
        }elseif($code_petugas>0){
            $petugas->delete_by_code_petugas($code_petugas);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Petugas deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Petugas delete failed.';
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