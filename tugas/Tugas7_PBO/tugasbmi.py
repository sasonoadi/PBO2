class PersonMeta(type):
    def __init__(cls, name, age,attrs):
        super().__init__(name,age,attrs)

        def data(cls,name,age):
            print(name, age)
        cls.data = classmethod(data)

class Person(metaclass=PersonMeta):
    pass

A=Person()
B=A.data('Roi',20)
print("data: ",B)

# Menambah atribut address secara dinamis
A.address = "Jalan Buah Mangga"

print(A.address)

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

weight = float(input("Masukkan berat badan (kg): "))
height = float(input("Masukkan tinggi badan (m): "))

hasil_bmi = calculate_bmi(weight, height)
print("BMI Anda adalah: ",hasil_bmi)

if hasil_bmi < 18.5:
    print("Anda termasuk dalam kategori Underweight (Kurus)")
elif 18.5 <= hasil_bmi < 25:
    print("Anda termasuk dalam kategori Normal (Ideal)")
elif 25 <= hasil_bmi < 30:
    print("Anda termasuk dalam kategori Overweight (Kelebihan Berat Badan)")
else:
    print("Anda termasuk dalam kategori Obese (Kegemukan)")
