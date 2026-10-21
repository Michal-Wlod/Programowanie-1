napoje = ["woda", "sok", "cola"]
ceny = [3, 5, 6]

i = 0
while i < len(napoje):
    print(f"{i+1}. {napoje[i]} - {ceny[i]}")
    i+=1
print("0. Zakończ")

cena_c = 0
while True:
    poz = int(input("wybierz pozycje: "))
    if poz > len(napoje) or poz < 0:
        print("wybrano nieprawidłowy artykuł")
        poz = int(input("wybierz pozycje: "))
    if poz == 0:
        break
    if poz>0 and poz<len(napoje)+1:
        cena_c += ceny[poz-1]
        print(f"Wybrano {napoje[poz-1]} - {ceny[poz-1]}zł")
print(f"Cena całkowita: {cena_c}")

