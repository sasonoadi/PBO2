class Univ:

    def __init__(self, nama_univ):
        self.nama_univ = nama_univ

    def desc(self):
        print(f'Universitas\t: {self.nama_univ}')


class Fakultas(Univ):

    def __init__(self, nama_univ, nama_fakultas, nama_prodi):
        super().__init__(nama_univ)
        self.nama_fakultas = nama_fakultas
        self.nama_prodi = nama_prodi

    def desc(self):
        super().desc()
        print(f'Fakultas\t: {self.nama_fakultas}')
        print(f'Program studi\t: {self.nama_prodi}')

class Gedung(Univ):

    def __init__(self, nama_gedung):
        self.nama_gedung = nama_gedung

    def desc(self):
        super().desc()
        print(f'Gedung\t\t: {self.nama_gedung}')


class Mahasiswa(Gedung, Fakultas):

    def __init__(self, nama_mhsw, nim, nama_univ, nama_fakultas, nama_prodi, nama_gedung):
        Fakultas.__init__(self, nama_univ, nama_fakultas, nama_prodi)
        Gedung.__init__(self, nama_gedung)
        self.nama_mhsw = nama_mhsw
        self.nim = nim

    def desc(self):
        super().desc()
        print(f"Nama\t\t: {self.nama_mhsw}")
        print(f"Nim\t\t: {self.nim}")


anto = Mahasiswa('Ericnam', '160202', 'Universitas Gajah Mada', 'Teknik', 'Teknik Kimia', 'Bungtomo')
anto.desc()