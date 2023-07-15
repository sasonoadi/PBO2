car=['Avanza','Xenia','Freed','Brio','GrandMax']
try:
    name=input("Masukan mobil: "))
    print(car[name])
    print("Mobil tersedia")
except IndexError:
    print("mobil tidak ada")