try:
    file = open("data.txt", "r")
    num = int(file.readline())
except ValueError:
    print("Error: Input tidak valid!")
finally:
    file.close()