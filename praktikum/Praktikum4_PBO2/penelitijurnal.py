class Jurnal:
    def __init__(self, judul, tahun):
        self.judul = judul
        self.tahun = tahun

class Peneliti:
    def __init__(self, nama, jurnal):
        self.nama = nama
        self.jurnal = jurnal

    def daftar_jurnal(self):
        for jurnal in self.jurnal:
            print(jurnal.judul, jurnal.tahun)

jurnal1 = Jurnal("Jaringan Komputer", "2012")
jurnal2 = Jurnal("Sistem Operasi", "2016")

peneliti = Peneliti("Thomas Alfa Edison", [jurnal1, jurnal2])
peneliti.daftar_jurnal()