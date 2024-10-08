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
sorszam = int(input("Adja meg egy vásárlás sorszámát! "))
arucikk = input("Adja meg egy árucikk nevét! ")
darabszam = int(input("Adja meg a vásárolt darabszámot! "))

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

counter = len(targyak) # 141
for i in range((len(targyak)) - 1, 0, -1): # 140 ---> 1
    if arucikk not in targyak[i]: # 1. eset: a kefe NINCS BENNE a targyak[140]?
        counter -= 1
    else:
        print(f"Az utolsó vásárlás sorszáma: {counter} ")
        break

print(f"{szamlalo} vásárlás során vettek belőle.")

# HF

print("\n7. feladat")

for kosar in targyak[sorszam - 1].items():
    print(kosar)
    # HF kiírás megcsinálása, növekvő sorrendben