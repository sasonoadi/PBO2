<?php
//Simpanlah dengan nama file : Anggota.php
require_once 'database.php';
class Anggota 
{
    private $db;
    private $table = 'anggota';
    public $code_anggota = "";
    public $nama = "";
    public $jk_anggota = "";
    public $jurusan = "";
    public $no_tlp = "";
    public $alamat = "";
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
    public function get_by_code_anggota(int $code_anggota)
    {
        $query = "SELECT * FROM $this->table WHERE code_anggota = $code_anggota";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`code_anggota`,`nama`,`jk_anggota`,`jurusan`,`no_tlp`,`alamat`) VALUES ('$this->code_anggota','$this->nama','$this->jk_anggota','$this->jurusan','$this->no_tlp','$this->alamat')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET code_anggota = '$this->code_anggota', nama = '$this->nama', jk_anggota = '$this->jk_anggota', jurusan = '$this->jurusan', no_tlp = '$this->no_tlp', alamat = '$this->alamat' 
        WHERE kode_anggota = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_code_anggota($code_anggota): int
    {
        $query = "UPDATE $this->table SET code_anggota = '$this->code_anggota', nama = '$this->nama', jk_anggota = '$this->jk_anggota', jurusan = '$this->jurusan', no_tlp = '$this->no_tlp', alamat = '$this->alamat' 
        WHERE code_anggota = $code_anggota";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE kode_anggota = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_code_anggota($code_anggota): int
    {
        $query = "DELETE FROM $this->table WHERE code_anggota = $code_anggota";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>