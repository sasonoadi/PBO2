class PesawatTerbang:
    def __init__(self, maskapai, tujuan, jenis_pesawat):
        self.maskapai = maskapai
        self.tujuan = tujuan
        self.jenis_pesawat = jenis_pesawat

    def info(self):
        print(f"maskapai: {self.maskapai}\ntujuan: {self.tujuan}\njenis_pesawat: {self.jenis_pesawat} ")
    
pesawatA = PesawatTerbang("Garuda Indonesia", "Bali-Jakarta", "Boing-737")
pesawatA.info()