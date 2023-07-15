import requests
import json
class Buku:
    def __init__(self):
        self.__id=None
        self.__code_buku = None
        self.__judul = None
        self.__penulis = None
        self.__penerbit = None
        self.__tahun_terbit = None
        self.__stok_buku = None
        self.__url = "http://localhost/perpustakaan/buku_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def code_buku(self):
        return self.__code_buku
        
    @code_buku.setter
    def code_buku(self, value):
        self.__code_buku = value
    @property
    def judul(self):
        return self.__judul
        
    @judul.setter
    def judul(self, value):
        self.__judul = value
    @property
    def penulis(self):
        return self.__penulis
        
    @penulis.setter
    def penulis(self, value):
        self.__penulis = value
    @property
    def penerbit(self):
        return self.__penerbit
        
    @penerbit.setter
    def penerbit(self, value):
        self.__penerbit = value
    @property
    def tahun_terbit(self):
        return self.__tahun_terbit
        
    @tahun_terbit.setter
    def tahun_terbit(self, value):
        self.__tahun_terbit = value
    @property
    def stok_buku(self):
        return self.__stok_buku
        
    @stok_buku.setter
    def stok_buku(self, value):
        self.__stok_buku = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_code_buku(self, code_buku):
        url = self.__url+"?code_buku="+code_buku
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['kode_buku']
            self.__code_buku = item['code_buku']
            self.__judul = item['judul']
            self.__penulis = item['penulis']
            self.__penerbit = item['penerbit']
            self.__tahun_terbit = item['tahun_terbit']
            self.__stok_buku = item['stok_buku']
        return data
    def simpan(self):
        payload = {
            "code_buku":self.__code_buku,
            "judul":self.__judul,
            "penulis":self.__penulis,
            "penerbit":self.__penerbit,
            "tahun_terbit":self.__tahun_terbit,
            "stok_buku":self.__stok_buku
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_code_buku(self, code_buku):
        url = self.__url+"?code_buku="+code_buku
        payload = {
            "code_buku":self.__code_buku,
            "judul":self.__judul,
            "penulis":self.__penulis,
            "penerbit":self.__penerbit,
            "tahun_terbit":self.__tahun_terbit,
            "stok_buku":self.__stok_buku
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_code_buku(self,code_buku):
        url = self.__url+"?code_buku="+code_buku
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text