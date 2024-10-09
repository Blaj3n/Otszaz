# Érték függvény működése
def ertek(darabszam: int):
    ar1 = 500
    ar2 = 450
    ar3 = 400
    if darabszam <= 0:
        return 0
    elif darabszam == 1:
        return ar1
    elif darabszam == 2:
        return ar1 + ar2
    else:  #darabszam >= 3
        return ar1 + ar2 + (darabszam - 2) * ar3

'''
Az árképzés logikája
Árak:
Az első darab ára: 500 Ft
A második darab ára: 450 Ft
A harmadik darab ára és az összes további darab ára: 400 Ft
'''

'''
1. 1 db termék vásárlásánál az Összeg: 500 Ft
Kód:
    elif darabszam == 1:
    return ar1  # 500 Ft
'''
print("Ha csak 1 darabot vásárolunk: ", end="")
print(ertek(1))

'''
2. 2 db termék vásárlásánál az Összeg: 950 Ft
Összeg: 500 Ft (1. darab) + 450 Ft (2. darab) = 950 Ft
Kód:
    elif darabszam == 2:
        return ar1 + ar2  # 500 + 450 = 950 Ft
'''
print("Ha 2 darabot vásárolunk: ", end="")
print(ertek(2))

'''
3. Ha 3 vagy több darabot vásárolunk
Itt már be kell számolnunk, hogy az első két darabot külön áron vásároltuk meg.
Az összeg: 500 Ft (1. darab) + 450 Ft (2. darab) + 400 Ft (3. darab) + 400 Ft (4. darab) + 400 Ft (5. darab),
és így tovább.
Példa: 5 darab vásárlása

Az első darab ára: 500 Ft
A második darab ára: 450 Ft
A harmadik darab ára: 400 Ft
A negyedik és ötödik darab ára: 400 Ft (mivel minden további darab is 400 Ft)

Hogyan számoljuk ki a harmadik és a további darabokat?
Az első és második darab ára már benne van az összegben.
A harmadik darab (és az azt követő darabok) ára: mind 400 Ft.

Számítás:
    1. Összeg: 500 + 450 + (darabszam - 2) * 400
    2. Példa 5 darabra:
        darabszam 5 - 2 = 3 (Ez a harmadik, negyedik és ötödik darab)
        Az ár kiszámítása:  500 + 450 + (3 * 400)
                            500 + 450 + 1200 = 2150  
    Összegzés:
        darabszam - 2 arra szolgál, hogy kiszámoljuk, hány darab termék van, ami 400 Ft-ba kerül
        (a harmadik és az azt követő darabok).
        Ha például 5 darabot vásárolsz, akkor a harmadik, negyedik és ötödik darab árát számoljuk ki: 
        3 * 400
'''

print("Ha 5 darabot vásárolunk: ", end="")
print(ertek(5))

