import numpy as np

ceny = np.array([])
x = int(input("podaj liczbe produktów: "))
while x < 1:
    print("podano zła wartość.")
    x = int(input("podaj liczbe produktów: "))

for i in range(x):
    cena = int(input(f"podaj cene {i+1}: "))
    while cena < 0:
        print("cena nie może być ujemna.")
        cena = int(input(f"podaj cene {i+1}: "))
    ceny = np.append(ceny, cena)

rabat = int(input("podaj przezece w %"))

print(f"ceny początkowe: {ceny}")
ceny_rabat = ceny * (1 - rabat / 100)
print(f"ceny po rabacie: {ceny_rabat}")

print(f"suma cen przed rabatem: {np.sum(ceny)}")
print(f"suma cen po rabacie: {np.sum(ceny_rabat)}")
print(f"ceny powyżej 100zl po rabacie: {ceny_rabat[ceny_rabat > 100]}")
