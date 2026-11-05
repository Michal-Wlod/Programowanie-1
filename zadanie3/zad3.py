biblioteka = []
while True:
    print("===== Biblioteka =====")
    print("1. dodaj książke")
    print("2. wyświetl wszystkie książki")
    print("3. Wyporzycz książke")
    print("4. Zwróć książke")
    print("5. Usuń książke")
    print("0. Zakończ")
    print("======================")
    opcja = input("wybierz opcje: ")

    if opcja == "1":
        tytul = input("podaj tytul: ")
        autor = input("podaj autora: ")
        biblioteka.append({"tytul": tytul, "autor": autor, "dostępna": True})
        print("książka dodana")
    if opcja == "2":
        if not(biblioteka):
            print("biblioteka jest pusta")
        else:
            for i, ksiazka in enumerate(biblioteka):
                status = "dostępna" if ksiazka['dostępna'] else "Wypożyczona"
                print(f"{i}. Tytuł: {ksiazka['tytul']}, autor: {ksiazka['autor']} Status: {status}")
    if opcja == "3":
        if not(biblioteka):
            print("biblioteka jest pusta")
        x = int(input("podaj numer książki do wyporzyczenia"))
        if x >= 0 and x <= len(biblioteka):

            if biblioteka[x]['dostępna']:
                biblioteka[x]['dostępna'] = False
                print("wypożyczona")
            else:
                print("nie można wypożyczyć książki")
        else:
            print("podano nieprawidłowy numer")
    if opcja == "4":
        if not(biblioteka):
            print("biblioteka jest pusta")
        x = int(input("podaj numer książki do oddania"))
        if x >= 0 and x <= len(biblioteka):

            if biblioteka[x]['dostępna'] == False:
                biblioteka[x]['dostępna'] = True
                print("oddana")
            else:
                print("książka jest już oddana")
        else:
            print("podano nieprawidłowy numer")
    if opcja == "5":
        x = int(input("podaj nr książki do usuniecia: "))
        del biblioteka[x]
        print("książka została usunięta")
    if opcja == "0":
        break




