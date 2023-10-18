from PIL import Image
import numpy as np

# Zad.2

obrazek = Image.open("inicjaly.bmp")
print("---------- informacje o obrazie")
print("tryb:", obrazek.mode)
print("format:", obrazek.format)
print("rozmiar:", obrazek.size)

# Zad.3

obrazek = Image.open("inicjaly.bmp")
dane_obrazka = np.asarray(obrazek)
dane_obrazka_01 = dane_obrazka * 1
print(dane_obrazka_01)

obrazek_text = open('inicjaly.txt', 'w')
for rows in dane_obrazka_01:
    for item in rows:
        obrazek_text.write(str(item) + ' ')
    obrazek_text.write('\n')

obrazek_text.close()

# Zad.4a

dane_obrazka4a = np.asarray(obrazek)
print("---------------- informacje o tablicy obrazu----------------")
print("typ danych tablicy:", dane_obrazka4a.dtype)
print("rozmiar tablicy:", dane_obrazka4a.shape)
print("liczba elementow:", dane_obrazka4a.size)
print("wymiar tablicy:", dane_obrazka4a.ndim)
print("rozmiar wyrazu tablicy:",
      dane_obrazka4a.itemsize)

# Zad.4b

print("Adres 50,30:", dane_obrazka4a[30][50])
print("Adres 90,40:", dane_obrazka4a[40][90])
print("Adres 99,0:", dane_obrazka4a[0][99])

# inicjaly.bmp do porównania

ob_bmp = open('ob_bmp.txt', 'w')
for rows in dane_obrazka:
    for item in rows:
        ob_bmp.write(str(item) + ' ')
    ob_bmp.write('\n')

ob_bmp.close()

# Zad.5

inicjaly_bool = np.loadtxt("inicjaly.txt", dtype=np.bool_)

ob_bool = open('ob_bool.txt', 'w')
for rows in inicjaly_bool:
    for item in rows:
        ob_bool.write(str(item) + ' ')
    ob_bool.write('\n')

ob_bool.close()

# Zad.6

inicjaly_int = np.loadtxt("inicjaly.txt", dtype=np.uint8)

ob_uint8 = open('ob_uint8.txt', 'w')
for rows in inicjaly_int:
    for item in rows:
        ob_uint8.write(str(item) + ' ')
    ob_uint8.write('\n')

ob_uint8.close()

# Zad.6a

ob = Image.fromarray(inicjaly_int)
ob.show()
