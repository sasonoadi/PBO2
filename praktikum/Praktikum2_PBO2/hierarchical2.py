class Kendaraan:
    def __init__(self, nama):
        self.nama = nama

    def get_nama(self):
        return self.nama
    
class Kereta(Kendaraan):
    def __init__(self, nama, mesin):
        super().__init__(nama) 
        self.mesin = mesin

    def get_tipe(self):
        return self.mesin
    
class Pesawat(Kendaraan):
    def __init__(self, nama, tipe):
        super().__init__(nama) 
        self.tipe = tipe

    def get_tipe_pesawat(self):
        return self.tipe

# turunan Hierarchical Inheritance
class PesawatTwinJet(Pesawat):
    def __init__(self, nama, tipe, kecepatan):
        super().__init__(nama, tipe) 
        self.kecepatan = kecepatan
        
    def get_kecepatan(self):
        return self.kecepatan
    
pesawattwinjet = PesawatTwinJet ('Boeing', '737-800', '966.560 km/h')
print('Merek        : ',pesawattwinjet.get_nama())
print('Tipe Pesawat : ',pesawattwinjet.get_tipe_pesawat())
print('Kecepatan    : ',pesawattwinjet.get_kecepatan())