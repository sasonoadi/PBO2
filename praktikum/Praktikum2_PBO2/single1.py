class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def berjalan(self):
        print(f"{self.nama} Adi sedang berjalan.")

class Dokter(Manusia):
    def __init__(self, nama, umur, nip):
        super().__init__(nama, umur)
        self.nip = nip

    def mengoperasi(self):
        print(f"{self.nama} Umur {self.umur} dengan NIP {self.nip} sedang mengoperasi pasien.")
        
dokterA = Dokter("Adi", 35, "160202")
dokterA.berjalan()
dokterA.mengoperasi()