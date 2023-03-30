class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def belajar(self):
        print("NIM", self.nim, self.nama, "Sedang Mengikuti Kelas")

class Pengusaha:
    def __init__(self, nama, pengusaha):
        self.nama = nama
        self.pengusaha = pengusaha

    def Pengusaha(self):
        print(self.nama, "sedang mengembangkan APP ")

class MahasiswaPengusaha(Mahasiswa, Pengusaha):
    def __init__(self, nama, nim, pengusaha):
        Mahasiswa.__init__(self, nama, nim)
        Pengusaha.__init__(self, nama, pengusaha)

    def MengerjakanTugas(self):
        print(self.nama, "Mengerjakan Tugas")
        
mhs_pengusaha = MahasiswaPengusaha("Nisa Maharani", "160202", "IT")
mhs_pengusaha.belajar()
mhs_pengusaha.Pengusaha()
mhs_pengusaha.MengerjakanTugas()