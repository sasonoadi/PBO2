class Kalkulator:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def subtract(x, y):
        return x - y
    
    @staticmethod
    def multiply(x, y):
        return x * y
    
    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError("Tidak dapat membagi dengan nol.")
        return x/y
        
# Memanggil metode statis add() dan subtract() di dalam class math
print(Kalkulator.add(3, 4))         # Output: 7
print(Kalkulator.subtract(16, 13))  # Output: 3

# Memanggil metode statis multiply() dan divide() di dalam class math
print(Kalkulator.multiply(5, 5))    # Output: 25
print(Kalkulator.divide(12, 4))     # Output: 3.0