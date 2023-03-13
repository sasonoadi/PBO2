class Mobil:
    def __init__(self, merek, jenis):
        self.merek = merek
        self.jenis = jenis

    def info(self):
        print(f"Mobil {self.merek} berjenis {self.jenis}")


mobilA = Mobil("Honda", "MPV")
mobilA.info() # Output Mobil Honda berjenis MPV