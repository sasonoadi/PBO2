class Pakaian:
    def __init__(self,nama, jenis, merek, warna):
        self.nama = nama
        self.jenis = jenis
        self.merek = merek
        self.warna = warna

    def Melihat(self):
        print(f"{self.nama} sedang melihat {self.jenis}.")

class Celana(Pakaian):
    def __init__(self, nama, jenis, merek, warna, size):
        super().__init__(nama, jenis, merek, warna)
        self.size = size

    def Memakai(self):
        print(f"{self.nama} sedang memakai {self.jenis} Merek {self.merek} Warna {self.warna} Ukuran {self.size}.")
        
celanaA = Celana ("Nisa", "Jeans" , "H&M", "Hitam", "28")
celanaA.Melihat()
celanaA.Memakai()