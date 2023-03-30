class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def display_info(self):
        print(f"Nama\t   : {self.nama}")
        print(f"Umur\t   : {self.umur}")

class Seniman:
    def __init__(self, seniman, pendapatan):
        self.seniman = seniman
        self.pendapatan = pendapatan

    def display_info(self):
        print(f"Seniman: {self.seniman}")
        print(f"Pendapatan: {self.pendapatan}")

class Pelukis:
    def __init__(self, aliran):
        self.aliran = aliran

    def display_info(self):
        print(f"Aliran: {self.aliran}")

class PelukisSeniman(Orang, Seniman, Pelukis):
    def __init__(self, nama, umur, seniman, pendapatan, aliran):
        Orang.__init__(self, nama, umur)
        Seniman.__init__(self, seniman, pendapatan)
        Pelukis.__init__(self, aliran)

    def display_info(self):
        super().display_info()
        print(f"Seniman    : {self.seniman}")
        print(f"Pendapatan : {self.pendapatan}")
        print(f"Aliran     : {self.aliran}")
       

# contoh penggunaan
pelukisSeniman = PelukisSeniman("Nisa", 22, "Pelukis", "Rp. 80jt", "Realisme",)
pelukisSeniman.display_info()