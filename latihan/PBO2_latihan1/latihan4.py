class Buku:
    def __init__(self, judul, penulis, penerbit):
        self.judul = judul
        self.penulis = penulis
        self.penerbit = penerbit

    def info(self):
        print(f"Judul: {self.judul}\nPenulis: {self.penulis}\nPenerbit: {self.penerbit}")


bukuA = Buku("Harry potter and the philosopher's Stone", "J.K. Rowling", "Gramedia")
bukuA.info()

# Output    Judul: Harry potter and the philosopher's Stone
#           Penulis: J.K. Rowling
#           Penerbit: Gramedia       