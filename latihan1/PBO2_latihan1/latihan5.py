class PesawatTerbang:
    def __init__(self, maskapai, tujuan, tipe_pesawat):
        self.maskapai = maskapai
        self.tujuan = tujuan
        self.tipe_pesawat = tipe_pesawat

    def info(self):
        print(f"Maskapai: {self.maskapai}\nTujuan: {self.tujuan}\nTipe Pesawat: {self.tipe_pesawat}")


pesawatA = PesawatTerbang("Garuda Indonesia", "Bali - Jakarta", "Boing 737")
pesawatA.info()

# Output    Maskapai: Garuda Indonesia
#           Tujuan: Bali - Jakarta
#           Tipe Pesawat : Boing 737