x = int(input("podaj cene produktu:"))
y = int(input("podaj rabat (%):"))

if y < 0 or y > 100:
    print("Nieprawidłowa wartość rabatu!")
    y = int(input("podaj rabat (%):"))
    

print("cena początkowa:", x)
kwota_rabatu = (x*y)/100
print("kwota rabatu:", kwota_rabatu)
print("cena końcowa:", x - kwota_rabatu)

if y >= 20:
    print("Duża promocja!")
else:
    print("Standardowa promocja")