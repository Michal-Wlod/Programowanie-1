magazyn = {
    "Mysz": 5,
    "Klawiatura": 3,
    "Monitor": 2, }

while True:
    print("//////////////////////////////")
    print("1 - stan magazynu")
    print("2 - przyjęcie towaru")
    print("3 - wydanie towaru")
    print("0 - zakończenie")
    print("//////////////////////////////")


    wybor = int(input("Podaj wybor: "))
    if wybor == 1:
        for przedmiot, ilosc in magazyn.items():
            print(f"{przedmiot} - {ilosc}")

    if wybor == 2:
        produkt = str(input("Podaj produkt: "))
        ilosc = int(input("Podaj ilosc: "))
        if produkt in magazyn:
            magazyn[produkt] += ilosc
        else:
            magazyn[produkt] = ilosc

    if wybor == 3:
        produkt = str(input("Podaj produkt: "))
        if produkt in magazyn:
            ilosc = int(input("Podaj ilosc: "))
            if magazyn[produkt] >= ilosc:
                magazyn[produkt] -= ilosc
            else:
                print("Nie ma tyle sztuk w magazynie.")
        else:
            print("Nie ma takiego produkt.")

    if wybor == 0:
        print("Do widzenia!")
        break


