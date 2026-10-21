zakupy = []

l = input("podaj liczbę produktów do dodania:")

for i in range (int(l)):
    produkt = input("dodaj produkt:")
    zakupy.append(produkt)
    print(zakupy)

u_prod = input("podaj produkt do usunięcia:")

if u_prod in zakupy:
    zakupy.remove(u_prod)
    print(zakupy)
else:
    print("nie znaleziono produkt")