# Nama: Adi Sasono
# NIM: 210511017
# Kelas: R1 (T121A)

class Celcius:
    def __init__(self, C):
        self.celcius = C

    def celcius_to_fahrenheit(self):
        F = (9/5) * self.celcius + 32
        return F
    
    def celcius_to_reamur(self):
        R = (4/5) * self.celcius
        return R
    
    def celcius_to_kelvin(self):
        K = self.celcius + 273
        return K
    
C_F = 75
celciusA = Celcius(C_F)
print("Konversi",C_F, "derajat celcius adalah:", celciusA.celcius_to_fahrenheit(), "derajat Farenheit\n")

C_R = 60
celciusB = Celcius(C_R)
print("Konversi",C_R, "derajat celcius adalah:", celciusB.celcius_to_reamur(), "derajat Reamur\n")

C_K = 90
celciusB = Celcius(C_K)
print("Konversi",C_R, "derajat celcius adalah:", celciusB.celcius_to_kelvin(), "derajat Kelvin\n")