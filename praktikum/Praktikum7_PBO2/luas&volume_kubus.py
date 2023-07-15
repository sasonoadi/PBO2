class KubusMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
# Tambahkan method untuk menghitung luas dan keliling kubus
        def luas(cls, rusuk ):
            return (rusuk * rusuk * 6)
        cls.luas = classmethod(luas)
        def volume(cls, rusuk):
            return (rusuk * rusuk * rusuk)
        cls.volume = classmethod(volume)
class Kubus(metaclass=KubusMeta):
    pass
s = Kubus()
# Menghitung luas rusuk dengan ruas=5
luas_kubus = Kubus.luas(5)
print("Luas Kubus:", luas_kubus)
# Menghitung volume rusuk dengan ruas=5
volume_kubus = Kubus.volume( 5)
print("volume kubus:", volume_kubus)