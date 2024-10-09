# print("1. feladat")
targyak = []
kosar = {}

with open("penztar.txt", "r", encoding="utf-8") as file:
    for egysor in file:
        if egysor.strip() != "F":
            if egysor.strip() not in kosar:     # egysor.strip() = "toll"
                kosar[egysor.strip()] = 1
            else:
                kosar[egysor.strip()] += 1
        elif egysor.strip() == "F":
            targyak.append(kosar)
            kosar = {}
print(targyak)

print("")

print("2. feladat")

szamlalo = 0
for egykosar in targyak:
    szamlalo += 1
print(f"A fizetések száma: {szamlalo}")

print("\n3. feladat")
elso_vasarlo = 0
for cikk in targyak[0].values():
    elso_vasarlo += cikk
print(f"Az első vásárló {elso_vasarlo} darab árucikket vásárolt.")
# print(targyak[0].items())
# print(targyak[0].keys())
# print(targyak[0].values())

print("\n4. feladat")
sorszam = 2#int(input("Adja meg egy vásárlás sorszámát! "))
arucikk = "kefe"#input("Adja meg egy árucikk nevét! ")
darabszam = 2#int(input("Adja meg a vásárolt darabszámot! "))

print("\n5. feladat")

szamlalo = 0
for kosar in targyak:
    for elem in kosar:
        if arucikk == elem:
            szamlalo += 1
# print(szamlalo)

szamolo = 1
for kosar in targyak:
    if arucikk not in kosar:
        szamolo += 1
    else:
        print(f"Az első vásárlás sorszáma: {szamolo} ")
        break

counter = len(targyak)  # 141
for i in range((len(targyak)) - 1, 0, -1):  # 140 ---> 1
    if arucikk not in targyak[i]:   # 1. eset: a kefe NINCS BENNE a targyak[140]?
        counter -= 1
    else:
        print(f"Az utolsó vásárlás sorszáma: {counter} ")
        break

print(f"{szamlalo} vásárlás során vettek belőle.")

print("\n6. feladat")


# minden arucikk = 500, arucikk > 1 = 450 arucikk > 2 = 400
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

print(f"{darabszam} darab vételekor fizetendő: {ertek(darabszam)}")


# # Példa a függvény használatára
# print(ertek(2))  # 950
# print(ertek(3))  # 1350
# print(ertek(5))  # 1850

print("\n7. feladat")

for kosar in targyak[sorszam - 1].items():
    print(kosar)
    # HF kiírás megcsinálása, növekvő sorrendben