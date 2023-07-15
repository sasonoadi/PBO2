import requests
import json
class Petugas:
    def __init__(self):
        self.__id=None
        self.__code_petugas = None
        self.__nama = None
        self.__jk_petugas = None
        self.__jabatan = None
        self.__no_telepon = None
        self.__alamat = None
        self.__url = "http://localhost/perpustakaan/petugas_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def code_petugas(self):
        return self.__code_petugas
        
    @code_petugas.setter
    def code_petugas(self, value):
        self.__code_petugas = value
    @property
    def nama(self):
        return self.__nama
        
    @nama.setter
    def nama(self, value):
        self.__nama = value
    @property
    def jk_petugas(self):
        return self.__jk_petugas
        
    @jk_petugas.setter
    def jk_petugas(self, value):
        self.__jk_petugas = value
    @property
    def jabatan(self):
        return self.__jabatan
        
    @jabatan.setter
    def jabatan(self, value):
        self.__jabatan = value
    @property
    def no_telepon(self):
        return self.__no_telepon
        
    @no_telepon.setter
    def no_telepon(self, value):
        self.__no_telepon = value
    @property
    def alamat(self):
        return self.__alamat
        
    @alamat.setter
    def alamat(self, value):
        self.__alamat = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_code_petugas(self, code_petugas):
        url = self.__url+"?code_petugas="+code_petugas
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['kode_petugas']
            self.__code_petugas = item['code_petugas']
            self.__nama = item['nama']
            self.__jk_petugas = item['jk_petugas']
            self.__jabatan = item['jabatan']
            self.__no_telepon = item['no_telepon']
            self.__alamat = item['alamat']
        return data
    def simpan(self):
        payload = {
            "code_petugas":self.__code_petugas,
            "nama":self.__nama,
            "jk_petugas":self.__jk_petugas,
            "jabatan":self.__jabatan,
            "no_telepon":self.__no_telepon,
            "alamat":self.__alamat
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_code_petugas(self, code_petugas):
        url = self.__url+"?code_petugas="+code_petugas
        payload = {
            "code_petugas":self.__code_petugas,
            "nama":self.__nama,
            "jk_petugas":self.__jk_petugas,
            "jabatan":self.__jabatan,
            "no_telepon":self.__no_telepon,
            "alamat":self.__alamat
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_code_petugas(self,code_petugas):
        url = self.__url+"?code_petugas="+code_petugas
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text