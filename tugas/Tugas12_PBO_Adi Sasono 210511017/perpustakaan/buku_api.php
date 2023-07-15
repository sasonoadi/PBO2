<?php
require_once 'database.php';
require_once 'Buku.php';
$db = new MySQLDatabase();
$buku = new Buku($db);
$id=0;
$code_buku=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['code_buku'])){
            $code_buku = $_GET['code_buku'];
        }
        if($id>0){    
            $result = $buku->get_by_id($id);
        }elseif($code_buku>0){
            $result = $buku->get_by_code_buku($code_buku);
        } else {
            $result = $buku->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new buku
        $buku->code_buku = $_POST['code_buku'];
        $buku->judul = $_POST['judul'];
        $buku->penulis = $_POST['penulis'];
        $buku->penerbit = $_POST['penerbit'];
        $buku->tahun_terbit = $_POST['tahun_terbit'];
        $buku->stok_buku = $_POST['stok_buku'];
       
        $buku->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Buku created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Buku not created.';
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
        if(isset($_GET['code_buku'])){
            $code_buku = $_GET['code_buku'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $buku->code_buku = $_PUT['code_buku'];
        $buku->judul = $_PUT['judul'];
        $buku->penulis = $_PUT['penulis'];
        $buku->penerbit = $_PUT['penerbit'];
        $buku->tahun_terbit = $_PUT['tahun_terbit'];
        $buku->stok_buku = $_PUT['stok_buku'];
        if($id>0){    
            $buku->update($id);
        }elseif($code_buku<>""){
            $buku->update_by_code_buku($code_buku);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Buku updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Buku update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['code_buku'])){
            $code_buku = $_GET['code_buku'];
        }
        if($id>0){    
            $buku->delete($id);
        }elseif($code_buku>0){
            $buku->delete_by_code_buku($code_buku);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Buku deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Buku delete failed.';
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