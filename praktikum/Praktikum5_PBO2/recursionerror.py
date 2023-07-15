#RecursionError adalah pengecualian yang terjadi ketika kedalaman rekursi maksimum terlampaui. 
#Ini biasanya terjadi ketika suatu fungsi memanggil dirinya sendiri secara rekursif, dan rekursi tidak memiliki kondisi penghentian yang tepat (kasus dasar).

def func():
    func()

func()
