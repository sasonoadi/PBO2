<?php
//Simpanlah dengan nama file : Petugas.php
require_once 'database.php';
class Petugas 
{
    private $db;
    private $table = 'petugas';
    public $code_petugas = "";
    public $nama = "";
    public $jk_petugas = "";
    public $jabatan = "";
    public $no_telepon = "";
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
    public function get_by_code_petugas(int $code_petugas)
    {
        $query = "SELECT * FROM $this->table WHERE code_petugas = $code_petugas";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`code_petugas`,`nama`,`jk_petugas`,`jabatan`,`no_telepon`,`alamat`) VALUES ('$this->code_petugas','$this->nama','$this->jk_petugas','$this->jabatan','$this->no_telepon','$this->alamat')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET code_petugas = '$this->code_petugas', nama = '$this->nama', jk_petugas = '$this->jk_petugas', jabatan = '$this->jabatan', no_telepon = '$this->no_telepon', alamat = '$this->alamat' 
        WHERE kode_petugas = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_code_petugas($code_petugas): int
    {
        $query = "UPDATE $this->table SET code_petugas = '$this->code_petugas', nama = '$this->nama', jk_petugas = '$this->jk_petugas', jabatan = '$this->jabatan', no_telepon = '$this->no_telepon', alamat = '$this->alamat' 
        WHERE code_petugas = $code_petugas";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE kode_petugas = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_code_petugas($code_petugas): int
    {
        $query = "DELETE FROM $this->table WHERE code_petugas = $code_petugas";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>