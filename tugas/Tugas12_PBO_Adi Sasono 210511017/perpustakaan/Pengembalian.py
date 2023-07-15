import requests
import json
class Pengembalian:
    def __init__(self):
        self.__id=None
        self.__code_pengembalian = None
        self.__tanggal_kembali = None
        self.__batas_tgl_kembali = None
        self.__denda_per_hari = None
        self.__jumlah_hari = None
        self.__total_denda = None
        self.__kode_anggota = None
        self.__kode_buku = None
        self.__kode_petugas = None
        self.__url = "http://localhost/perpustakaan/pengembalian_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def code_pengembalian(self):
        return self.__code_pengembalian
        
    @code_pengembalian.setter
    def code_pengembalian(self, value):
        self.__code_pengembalian = value
    @property
    def tanggal_kembali(self):
        return self.__tanggal_kembali
        
    @tanggal_kembali.setter
    def tanggal_kembali(self, value):
        self.__tanggal_kembali = value
    @property
    def batas_tgl_kembali(self):
        return self.__batas_tgl_kembali
        
    @batas_tgl_kembali.setter
    def batas_tgl_kembali(self, value):
        self.__batas_tgl_kembali = value
    @property
    def denda_per_hari(self):
        return self.__denda_per_hari
        
    @denda_per_hari.setter
    def denda_per_hari(self, value):
        self.__denda_per_hari = value
    @property
    def jumlah_hari(self):
        return self.__jumlah_hari
        
    @jumlah_hari.setter
    def jumlah_hari(self, value):
        self.__jumlah_hari = value
    @property
    def total_denda(self):
        return self.__total_denda
        
    @total_denda.setter
    def total_denda(self, value):
        self.__total_denda = value
    @property
    def kode_anggota(self):
        return self.__kode_anggota
        
    @kode_anggota.setter
    def kode_anggota(self, value):
        self.__kode_anggota = value
    @property
    def kode_buku(self):
        return self.__kode_buku
        
    @kode_buku.setter
    def kode_buku(self, value):
        self.__kode_buku = value
    @property
    def kode_petugas(self):
        return self.__kode_petugas
        
    @kode_petugas.setter
    def kode_petugas(self, value):
        self.__kode_petugas = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_code_pengembalian(self, code_pengembalian):
        url = self.__url+"?code_pengembalian="+code_pengembalian
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['kode_kembali']
            self.__code_pengembalian = item['code_pengembalian']
            self.__tanggal_kembali = item['tanggal_kembali']
            self.__batas_tgl_kembali = item['batas_tgl_kembali']
            self.__denda_per_hari = item['denda_per_hari']
            self.__jumlah_hari = item['jumlah_hari']
            self.__total_denda = item['total_denda']
            self.__kode_anggota = item['kode_anggota']
            self.__kode_buku = item['kode_buku']
            self.__kode_petugas = item['kode_petugas']
        return data
    def simpan(self):
        payload = {
            "code_pengembalian":self.__code_pengembalian,
            "tanggal_kembali":self.__tanggal_kembali,
            "batas_tgl_kembali":self.__batas_tgl_kembali,
            "denda_per_hari":self.__denda_per_hari,
            "jumlah_hari":self.__jumlah_hari,
            "total_denda":self.__total_denda,
            "kode_anggota":self.__kode_anggota,
            "kode_buku":self.__kode_buku,
            "kode_petugas":self.__kode_petugas
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_code_pengembalian(self, code_pengembalian):
        url = self.__url+"?code_pengembalian="+code_pengembalian
        payload = {
            "code_pengembalian":self.__code_pengembalian,
            "tanggal_kembali":self.__tanggal_kembali,
            "batas_tgl_kembali":self.__batas_tgl_kembali,
            "denda_per_hari":self.__denda_per_hari,
            "jumlah_hari":self.__jumlah_hari,
            "total_denda":self.__total_denda,
            "kode_anggota":self.__kode_anggota,
            "kode_buku":self.__kode_buku,
            "kode_petugas":self.__kode_petugas
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_code_pengembalian(self,code_pengembalian):
        url = self.__url+"?code_pengembalian="+code_pengembalian
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
