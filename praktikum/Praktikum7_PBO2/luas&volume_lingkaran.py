class lingkaranMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
# Tambahkan method untuk menghitung luas dan keliling balok
        def luas(cls, r):
            return 22/7*r*r
        cls.luas = classmethod(luas)
        def volume(cls, r):
            return 22/7*r*r
        cls.volume = classmethod(volume)
class Lingkaran(metaclass=lingkaranMeta):
    pass
s = Lingkaran()
# Menghitung luas lingkaran dengan jari jari=4
luas_lingkaran = Lingkaran.luas(4)
print("Luas lingkaran:", luas_lingkaran)
# Menghitung volume dengan jari jari=7
volume_lingkaran = Lingkaran.volume(7)
print("volume lingkaran:", volume_lingkaran)