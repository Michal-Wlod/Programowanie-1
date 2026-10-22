operacje = []

while True:
    print("========== MOJ BUDZET ==========")
    print("1. Dodaj przychod")
    print("2. Dodaj wydatek")
    print("3. Wyswietl historie operacji")
    print("4. Wyswietl stan konta")
    print("5. Podsumowanie finansowe")
    print("7. Usun operacje")
    print("0. Zakoncz")
    print("================================")

    opcja = input("wybierz opcje: ")

    if opcja == "1":
        opis = input("opis przychodu: ")
        kwota = float(input("Podaj kwote: "))
        if kwota < 0:
            print("kwota musi być dodatnia")
            kwota = float(input("Podaj kwote: "))
        operacje.append({'typ': 'przychod', 'opis': opis, 'kwota': kwota})
        print("Przychod dodany.")

    if opcja == "2":
        opis = input("opis wydatku: ")
        kwota = float(input("Podaj kwote: "))
        if kwota < 0:
            print("kwota musi być dodatnia")
            kwota = float(input("Podaj kwote: "))
        operacje.append({'typ': 'wydatek', 'opis': opis, 'kwota': kwota})
        print("wydatek dodany.")
    if opcja == "3":
        numer = 0
        for i in operacje:
            print(f"{numer} - {i}")
            numer += 1
    if opcja == "4":
        suma = 0
        for i, typ in enumerate(operacje):
            if typ['typ'] == 'przychod':
                suma += operacje[i]['kwota']
            elif typ['typ'] == 'wydatek':
                suma -= operacje[i]['kwota']
        print(suma)
    if opcja == "5":
        suma_p = 0
        suma_w = 0
        for i, typ in enumerate(operacje):
            if typ['typ'] == 'przychod':
                suma_p += operacje[i]['kwota']

            if typ['typ'] == 'wydatek':
                suma_w += operacje[i]['kwota']
            elif not typ['typ'] == 'wydatek':
                print("brak wydatków")
            print(f"suma przychod: {suma_p}")
            print(f"suma wydatków: {suma_w}")
            print(f"bilans: {suma_p - suma_w}")
            print(f"najwięwszy wydatek")
    if opcja == "6":
        num = int(input("Podaj numer operacji do usunięcia: "))
        if num > 0 and num <= len(operacje):
            operacje.pop(num)
            print("operacja usunienta")
        else:
            print("nieprawidłowy numer")

    if opcja == "0":
        break