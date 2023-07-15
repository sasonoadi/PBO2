class Mahasiswa:
    def __init__(self, nama, jurusan):
        self.nama = nama
        self.jurusan = jurusan

class KelompokKKM:
    def __init__(self, kelompok, mahasiswa):
        self.kelompok = kelompok
        self.mahasiswa = mahasiswa

    def daftar_mahasiwa(self):
        for mahasiswa in self.mahasiswa:
            print(mahasiswa.nama, mahasiswa.jurusan)

mahasiswa1 = Mahasiswa("Brownie Sofa", "Teknik Industri")
mahasiswa2 = Mahasiswa("Softa Andre", "Akuntansi")

kelompok1 = KelompokKKM("Kelompok 1", [mahasiswa1, mahasiswa2])
kelompok1.daftar_mahasiwa()