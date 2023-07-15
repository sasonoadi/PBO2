class Barang:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

class Toko:
    def __init__(self, nama, barang):
        self.nama = nama
        self.barang = barang

    def daftar_barang(self):
        for barang in self.barang:
            print(barang.nama, barang.harga)

barang1 = Barang("Shampoo Rejoice", "1000")
barang2 = Barang("Sabun Dettol", "4000")

penulis = Toko("Toko Alhamdulillah", [barang1, barang2])
penulis.daftar_barang()