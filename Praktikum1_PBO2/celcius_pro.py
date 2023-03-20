# Nama: Adi Sasono
# NIM: 210511017
# Kelas: R1 (T121A)

class Suhu:
    @staticmethod
    def celcius_to_fahrenheit(C):
        F = (9/5) * C + 32
        return F

    @staticmethod
    def celcius_to_reamur(C):
        R = (4/5) * C
        return R
    
    @staticmethod
    def celcius_to_kelvin(C):
        K = C + 273
        return K


C = 75
F = Suhu.celcius_to_fahrenheit(C)
print("Konversi",C, "derajat Celcius adalah:",F, "derajat Fahrenheit")

C = 60
R = Suhu.celcius_to_reamur(C)
print("Konversi",C, "derajat Celcius adalah:",R, "derajat Reamur")

C = 90
K = Suhu.celcius_to_kelvin(C)
print("Konversi",C, "derajat Celcius adalah:",K, "derajat Kelvin")