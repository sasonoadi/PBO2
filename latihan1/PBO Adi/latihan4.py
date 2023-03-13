class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit

    def info(self):
        print(f"judul: {self.judul}\npenulis: {self.penulis}\ntahun_terbit: {self.tahun_terbit}")

bukuA = Buku("Harry potter and the philosopher's stone","J.K. Rowling", "2011")
bukuA.info()