class Celcius:
    @staticmethod
    def to_fahrenheit(celcius):
        return (celcius * 9/5) + 32
    
    @staticmethod
    def to_kelvin(celcius):
        return celcius + 273.15
    
    @staticmethod
    def to_reamur(celsius):
        return celsius * 4/5
    
mycelcius = 90
myfahrenheit = Celcius.to_fahrenheit(mycelcius)
mykelvin = Celcius.to_kelvin(mycelcius)
print(myfahrenheit)
print(mykelvin)

# Output 194.0