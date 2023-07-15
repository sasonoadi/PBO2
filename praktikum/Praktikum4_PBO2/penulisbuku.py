class Buku:
    def __init__(self, judul, tahun):
        self.judul = judul
        self.tahun = tahun

class Penulis:
    def __init__(self, nama, buku):
        self.nama = nama
        self.buku = buku

    def daftar_buku(self):
        for buku in self.buku:
            print(buku.judul, buku.tahun)

buku1 = Buku("Harry Potter and The Chamber Of Secret", "2002")
buku2 = Buku("Bagaimana Cara Menjadi Aku", "2016")

penulis = Penulis("Browna Sofi", [buku1, buku2])
penulis.daftar_buku()