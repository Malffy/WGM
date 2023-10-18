from PIL import Image
import numpy as np

# Zad_1

def rysuj_ramke_w_ramce_szare(w, h, grub, kolor):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    temp = 1
    minimum = min(w, h)
    end = int(minimum/(2*grub))
    for i in range(0, end):
        tab[temp*grub: h - (temp * grub), temp*grub: w - (temp*grub)] = kolor % 256
        temp += 1
        kolor += 50
    return Image.fromarray(tab)

obraz_1 = rysuj_ramke_w_ramce_szare(120,60,8,100)
obraz_1.save("obraz_1.bmp")
obraz_1.show()


def rysuj_pasy_pionowe(w, h, grub, kolor):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w/grub)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                tab[j, i] = k % 2
                kolor += 25
    return Image.fromarray(tab)

obraz_2 = rysuj_pasy_pionowe(100, 100, 20, 50)
obraz_2.save("obraz_2.bmp")
obraz_2.show()