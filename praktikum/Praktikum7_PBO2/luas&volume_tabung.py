class TabungMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
# Tambahkan method untuk menghitung luas dan keliling tabung tanpa tutup
        def luas(cls, r, t ):
            return (2 * 22/7 * r * t)+(22/7 *r *r)
        cls.luas = classmethod(luas)
        def volume(cls, r, t):
            return (22/7 * r* r * t)
        cls.volume = classmethod(volume)
class Tabung(metaclass=TabungMeta):
    pass
s = Tabung()
# Menghitung luas rusuk dengan ruas=5 tinggi=10
luas_tabung = Tabung.luas(2, 5)
print("Luas Tabung:", luas_tabung)
# Menghitung volume rusuk dengan ruas=5 tinggi=10
volume_tabung = Tabung.volume(2, 5)
print("volume Tabung:", volume_tabung)