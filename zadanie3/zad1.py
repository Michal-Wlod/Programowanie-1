kontakty = {}

while True:
    print("========== KISAZKA KONTAKTÓW ===========")
    print("1. Dodaj kontakt")
    print("2. Wyświetl wszystkie kontakty")
    print("3. Wyszukaj kontakt")
    print("4. Edytuj kontakt")
    print("5. Usuń kontakt")
    print("0.  zakończ")
    print("========================================")

    opcja = input("Wybierz opcje: ")

    if opcja == "1":
        imie = str(input("Podaj imie:"))
        nazwisko = str(input("Podaj nazwisko:"))
        telefon = str(input("Podaj numer:"))
        if telefon in kontakty:
            print("błąd kontakt z tym numerem już istnieje")
        else:
            kontakty[telefon] = [imie, nazwisko]
    if opcja == "2":
        if not kontakty:
            print("książka kontaktów jest pusta")
        else:
            for tel, dane in kontakty.items():
                print(f"imie: {dane[0]}")
                print(f"nazwisko: {dane[1]}")
                print(f"Telefon: {tel}")
    if opcja == "3":
        numer = str(input("Podaj numer:"))
        if numer in kontakty:
            dane = kontakty[numer]
            print(f"imie: {dane[0]}")
            print(f"nazwisko: {dane[1]}")
        else:
            print("nie znaleziono kontaktu")
    if opcja == "4":
        telefon = str(input("Podaj numer do edycji:"))
        if telefon in kontakty:
            imie = str(input("Podaj nowe imie:"))
            nazwisko = str(input("Podaj nowe nazwisko:"))
            kontakty[telefon] = [imie, nazwisko]
            print("kontakt zaktualizowany")
        else:
            print("nie znaleziono kontaktu")
    if opcja == "5":
        telefon = str(input("Podaj numer do usunięcia:"))
        if telefon in kontakty:
            del kontakty[telefon]
            print("kontakt usunięty")
        else:
            print("nie znaleziono kontaktu")
    if opcja == "0":
        break


