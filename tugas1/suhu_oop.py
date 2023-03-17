# Nama  : Adi Sasono
# NIM   : 210511017
# Kelas : R1 (TA21A)

class Fahrenheit:
    def __init__(self, F):
        self.Fahrenheit = F

    def fahrenheit_to_celcius(self):
        C = (5/9) * self.Fahrenheit - 32
        return C
    
    def fahrenheit_to_reamure(self):
        R = (4/9) * self.Fahrenheit - 32
        return R
    
    def fahrenheit_to_kelvin(self):
        K = (5/9) * self.Fahrenheit + 273
        return K
    
print("~"*85) 
F = int(input("Masukkan Farenheit: "))
fahrenheit = Fahrenheit(F)
print("")
print("Konversi",F, "derajat Fahrenheit adalah:", fahrenheit.fahrenheit_to_celcius(), "derajat Celcius.")
print("Konversi",F, "derajat Fahrenheit adalah:", fahrenheit.fahrenheit_to_reamure(), "derajat Reamure.")
print("Konversi",F, "derajat Fahrenheit adalah:", fahrenheit.fahrenheit_to_kelvin(), "derajat Kelvin.")
print("~"*85)

# Nama  : Adi Sasono
# NIM   : 21051101
# Kelas : R1 (TA21A)

class Reamure:
    def __init__(self, R):
        self.Reamure = R

    def reamure_to_celcius(self):
        C = self.Reamure / 0.8
        return C
    
    def reamure_to_fahrenheit(self):
        R = (self.Reamure * 2.25) + 32
        return R
    
    def reamure_to_kelvin(self):
        K = (self.Reamure / 0.8) + 273.15
        return K

R = int(input("Masukkan Reamure: "))
reamure = Reamure(R)
print("")
print("Konversi",R, "derajat Reamure adalah:",reamure.reamure_to_celcius(), "derajat Celcius.")
print("Konversi",R, "derajat Reamure adalah:",reamure.reamure_to_fahrenheit(), "derajat Fahrenheit.")
print("Konversi",R, "derajat Reamure adalah:",reamure.reamure_to_kelvin(), "derajat Kelvin.")
print("~"*85)

# Nama  : Adi Sasono
# NIM   : 210511017
# Kelas : R1 (TA21A)

class Kelvin:
    def __init__(self, K):
        self.Kelvin = K

    def kelvin_to_celcius(self):
        C = self.Kelvin - 273.15
        return C
    
    def kelvin_to_fahrenheit(self):
        F = (self.Kelvin * 9/5) - 459.67
        return F
    
    def kelvin_to_reamure(self):
        R = 4/5 * (self.Kelvin - 273)
        return R

K = int(input("Masukkan Kelvin: "))
kelvin = Kelvin(K)
print("")
print("Konversi",K, "derajat kelvin adalah:",kelvin.kelvin_to_celcius(), "derajat Celcius.")
print("Konversi",K, "derajat Kelvin adalah:",kelvin.kelvin_to_fahrenheit(), "derajat Fahrenheit.")
print("Konversi",K, "derajat Kelvin adalah:",kelvin.kelvin_to_reamure(), "derajat Reamure.")
print("~"*85)
