x = int(input("podaj liczbe produktów: "))
l_p = []
l_c = []
for i in range(x):
    nazwa = str(input("podaj nazwe produktu: "))
    cena = int(input("podaj cene produktu: "))
    l_p.append(nazwa)
    l_c.append(cena)



for numer, nazwa in enumerate(l_p, start=1):
    print(f"{numer}. {nazwa}")


x = 1
print("cennik: ")
for produkt, cena in zip(l_p, l_c):
    print(f"{x}. {produkt} - {cena}zł")
    x+=1

suma = 0
for i in range(len(l_p)):
    suma += l_c[i]
print(f"suma: {suma}")

cena_max = max(l_c)
max_cena = l_c.index(cena_max)
produkt_max = l_p[max_cena]

print(f"najdroższy produkt: {produkt_max} - {cena_max} zł")