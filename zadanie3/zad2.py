dzialania = []
while True:
    print("===== Kalkulator =====")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Potęgowanie")
    print("6. Średnia")
    print("0. Zakończ")
    print("======================")

    opcja = input("Podaj opcje: ")

    if opcja == "1":
        a = int(input("Podaj a: "))
        b = int(input("Podaj b: "))
        wynik = a+b
        print(wynik)

        dzialania.append(wynik)

    if opcja == "2":
        a = int(input("Podaj a: "))
        b = int(input("Podaj b: "))
        wynik = a-b
        print(wynik)

        dzialania.append(wynik)

    if opcja == "3":
        a = int(input("Podaj a: "))
        b = int(input("Podaj b: "))
        wynik = a*b
        print(wynik)

        dzialania.append(wynik)

    if opcja == "4":
        a = int(input("Podaj a: "))
        b = int(input("Podaj b: "))
        if b == 0:
            print("nie dziel przez 0")
            b = int(input("Podaj b: "))

        wynik = a/b
        print(wynik)

        dzialania.append(wynik)



    if opcja == "5":
        a = int(input("Podaj a: "))
        b = int(input("Podaj b: "))
        wynik = a**b
        print(wynik)
        dzialania.append(wynik)

    if opcja == "6":
        print("liczby: ")
        for i in dzialania:
            print(i)


        wynik =  sum(dzialania) / len(dzialania)
        print(f"średnia: {wynik}")

    if opcja == "0":
        break



