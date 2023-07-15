import requests
import json
class Anggota:
    def __init__(self):
        self.__id=None
        self.__code_anggota = None
        self.__nama = None
        self.__jk_anggota = None
        self.__jurusan = None
        self.__no_tlp = None
        self.__alamat = None
        self.__url = "http://localhost/perpustakaan/anggota_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def code_anggota(self):
        return self.__code_anggota
        
    @code_anggota.setter
    def code_anggota(self, value):
        self.__code_anggota = value
    @property
    def nama(self):
        return self.__nama
        
    @nama.setter
    def nama(self, value):
        self.__nama = value
    @property
    def jk_anggota(self):
        return self.__jk_anggota
        
    @jk_anggota.setter
    def jk_anggota(self, value):
        self.__jk_anggota = value
    @property
    def jurusan(self):
        return self.__jurusan
        
    @jurusan.setter
    def jurusan(self, value):
        self.__jurusan = value
    @property
    def no_tlp(self):
        return self.__no_tlp
        
    @no_tlp.setter
    def no_tlp(self, value):
        self.__no_tlp = value
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
    def get_by_code_anggota(self, code_anggota):
        url = self.__url+"?code_anggota="+code_anggota
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['kode_anggota']
            self.__code_anggota = item['code_anggota']
            self.__nama = item['nama']
            self.__jk_anggota = item['jk_anggota']
            self.__jurusan = item['jurusan']
            self.__no_tlp = item['no_tlp']
            self.__alamat = item['alamat']
        return data
    def simpan(self):
        payload = {
            "code_anggota":self.__code_anggota,
            "nama":self.__nama,
            "jk_anggota":self.__jk_anggota,
            "jurusan":self.__jurusan,
            "no_tlp":self.__no_tlp,
            "alamat":self.__alamat
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_code_anggota(self, code_anggota):
        url = self.__url+"?code_anggota="+code_anggota
        payload = {
            "code_anggota":self.__code_anggota,
            "nama":self.__nama,
            "jk_anggota":self.__jk_anggota,
            "jurusan":self.__jurusan,
            "no_tlp":self.__no_tlp,
            "alamat":self.__alamat
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_code_anggota(self,code_anggota):
        url = self.__url+"?code_anggota="+code_anggota
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
