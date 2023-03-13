class Mobil:
    def __init__(self, merk, tipe):
        self.merk = merk
        self.tipe = tipe

    def info(self):
        print(f"Mobil {self.merk} bertipe {self.tipe}")

mobilA = Mobil("Honda", "cvt")
mobilA.info() # Output: Mobil Honda Bertipe cvt