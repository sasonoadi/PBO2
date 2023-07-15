<?php
//Simpanlah dengan nama file : Peminjaman.php
require_once 'database.php';
class Peminjaman 
{
    private $db;
    private $table = 'peminjaman';
    public $code_pinjam = "";
    public $tanggal_kembali = "";
    public $batas_tgl_kembali = "";
    public $denda_per_hari = "";
    public $jumlah_hari = "";
    public $total_denda = "";
    public $kode_anggota = "";
    public $kode_buku = "";
    public $kode_petugas = "";
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
    public function get_by_code_pinjam(int $code_pinjam)
    {
        $query = "SELECT * FROM $this->table WHERE code_pinjam = $code_pinjam";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`code_pinjam`,`tanggal_kembali`,`batas_tgl_kembali`,`denda_per_hari`,`jumlah_hari`,`total_denda`,`kode_anggota`,`kode_buku`,`kode_petugas`) VALUES ('$this->code_pinjam','$this->tanggal_kembali','$this->batas_tgl_kembali','$this->denda_per_hari','$this->jumlah_hari','$this->total_denda','$this->kode_anggota','$this->kode_buku','$this->kode_petugas')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET code_pinjam = '$this->code_pinjam', tanggal_kembali = '$this->tanggal_kembali', batas_tgl_kembali = '$this->batas_tgl_kembali', denda_per_hari = '$this->denda_per_hari', jumlah_hari = '$this->jumlah_hari', total_denda = '$this->total_denda', kode_anggota = '$this->kode_anggota', kode_buku = '$this->kode_buku', kode_petugas = '$this->kode_petugas' 
        WHERE kode_kembali = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_code_pinjam($code_pinjam): int
    {
        $query = "UPDATE $this->table SET code_pinjam = '$this->code_pinjam', tanggal_kembali = '$this->tanggal_kembali', batas_tgl_kembali = '$this->batas_tgl_kembali', denda_per_hari = '$this->denda_per_hari', jumlah_hari = '$this->jumlah_hari', total_denda = '$this->total_denda', kode_anggota = '$this->kode_anggota', kode_buku = '$this->kode_buku', kode_petugas = '$this->kode_petugas' 
        WHERE code_pinjam = $code_pinjam";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE kode_kembali = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_code_pinjam($code_pinjam): int
    {
        $query = "DELETE FROM $this->table WHERE code_pinjam = $code_pinjam";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>