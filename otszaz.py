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
sorszam = 2 #int(input("Adja meg egy vásárlás sorszámát! "))
arucikk = "kefe" #input("Adja meg egy árucikk nevét! ")
darabszam = 2 #int(input("Adja meg a vásárolt darabszámot! "))

print("\n5. feladat")

szamlalo = 0
for kosar in targyak:
    for elem in kosar:
        if arucikk == elem:
            szamlalo += 1
print(szamlalo)

szamolo = 1
for kosar in targyak:
    if arucikk not in kosar:
        szamolo += 1
    else:
        print(f"Az első vásárlás sorszáma: {szamolo} ")
        break


print("Az utolsó vásárlás sorszáma:")
print(f"{szamlalo} vásárlás során vettek belőle.")