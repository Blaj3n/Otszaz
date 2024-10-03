# A dictionary egy igen használatos adatstruktúra: {key: value}
# [{toll: 1}, {colostok: 2, HB ceruza: 2, ...}]
kosarak = {
    "termek": "alma",
    "db": 3,
    "év": 2024
}

# print(type(kosarak))
print(kosarak["db"])
kosarak["nev"] = "Bence"    # hozzáadja kosarak dictionary-hez a nev key-t és a hozzátartozó value-t, Lásd.: listánál az append.
print(kosarak.keys())       # visszaadja a dictionary kulcsait
print(kosarak.values())     # visszaadja a dictionary értékeit
print(kosarak.items())      # ezek az adott kosár kulcsai [0], és értékei [1]

i = 0
for egyelem in kosarak.items():     # végigjárjuk a kosarak nevű dict. adatait
    if i < 2:
        print(f"{egyelem[0]}: {egyelem[1]}")    # egyelem = (key: value)
        i += 1