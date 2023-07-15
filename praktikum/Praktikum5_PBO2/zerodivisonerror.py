try:
    a = 10
    b = 0
    print(a/b)
except ZeroDivisionError as e:
    print("Error: Cannot divide by zero")