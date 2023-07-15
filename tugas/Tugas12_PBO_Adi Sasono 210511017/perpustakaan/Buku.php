<?php
//Simpanlah dengan nama file : Buku.php
require_once 'database.php';
class Buku 
{
    private $db;
    private $table = 'buku';
    public $code_buku = "";
    public $judul = "";
    public $penulis = "";
    public $penerbit = "";
    public $tahun_terbit = "";
    public $stok_buku = "";
    public function __construct(MySQLDatabase $db)
    {
        $this->db = $db;
    }
    public function get_all() 
    {
        $query = "SELECT * FROM $this->table";
        $result_set = $this->db->query($query);
        return $result_set;
    }
    public function get_by_id(int $id)
    {
        $query = "SELECT * FROM $this->table WHERE id = $id";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function get_by_code_buku(int $code_buku)
    {
        $query = "SELECT * FROM $this->table WHERE code_buku = $code_buku";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`code_buku`,`judul`,`penulis`,`penerbit`,`tahun_terbit`,`stok_buku`) VALUES ('$this->code_buku','$this->judul','$this->penulis','$this->penerbit','$this->tahun_terbit','$this->stok_buku')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET code_buku = '$this->code_buku', judul = '$this->judul', penulis = '$this->penulis', penerbit = '$this->penerbit', tahun_terbit = '$this->tahun_terbit', stok_buku = '$this->stok_buku' 
        WHERE kode_buku = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_code_buku($code_buku): int
    {
        $query = "UPDATE $this->table SET code_buku = '$this->code_buku', judul = '$this->judul', penulis = '$this->penulis', penerbit = '$this->penerbit', tahun_terbit = '$this->tahun_terbit', stok_buku = '$this->stok_buku' 
        WHERE code_buku = $code_buku";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE kode_buku = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_code_buku($code_buku): int
    {
        $query = "DELETE FROM $this->table WHERE code_buku = $code_buku";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>