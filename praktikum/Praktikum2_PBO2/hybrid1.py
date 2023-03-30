class Rumahsakit:
  def __init__(self):
    self.rs = "Rumahsakit Cahaya Bunda"
  def display(self):
    print(f"Nama Rumahsakit\t\t: {self.rs}")


class Jabatan(Rumahsakit):
  def __init__(self):
    Rumahsakit.__init__(self)
    self.course = "Dokter Utama"
  def display(self):  
    print(f"Jabatan Dokter\t\t: {self.course}")
    Rumahsakit.display(self)


class Spesialis(Rumahsakit):
  def __init__(self):
    self.Spesialis = "Kandungan"
  def display(self):  
    print(f"Spesialis\t\t: {self.Spesialis}")


class Mahasiswa(Jabatan, Spesialis):
  def __init__(self):
    self.name = "Steven Eric"
    Spesialis.__init__(self)
    Jabatan.__init__(self)
  def display(self):
    print(f"Nama Dokter\t\t: {self.name}")
    Spesialis.display(self)
    Jabatan.display(self)


ob = Mahasiswa()  
print()
ob.display()