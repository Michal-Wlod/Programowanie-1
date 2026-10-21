zadania = []
wartosc = 1
while True:
    print(".....................")
    print("1 - Dodaj zadanie")
    print("2 - Wyświetl zadania")
    print("3 - Usuń zadanie")
    print("4 - Wyświetl liczbe zadań")
    print("0 - Zakończ")
    print(".....................")
    print(" ")

    x = int(input("Wybierz działanie: "))
    if x == 1:
        zad = str(input("Wpisz nazwe zadania: "))
        zadania.append(zad)
    elif x == 2:
        print("Obecne zadania : ")
        for wartosc, zadanie in enumerate(zadania, start=1):
            print(f"{wartosc} - {zadanie}")
            

    elif x == 3:
        usun = int(input("Podaj numer zadania do usunięcia: "))
        zadania.pop(usun-1)
    elif x == 4:
        print(f"ilość zadań: {len(zadania)}")
    elif x == 0:
        print("Do widzenia!")
        break