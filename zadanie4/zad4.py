warsztat_python = set()
warsztat_ai = set()

def pobierz_uczestnika():
    imie = str(input("podaj imie uczestnika: "))
    nazwisko = str(input("podaj nazwisko uczestnika: "))
    return (imie, nazwisko)


while True:
    print("1 - zapisz na Python")
    print("2 - zapisz na AI")
    print("3 - wyświetl uczestników")
    print("4 - uczestnicy oby warsztatów")
    print("5 - wszyscy unikalni uczestnicy")
    print("0 - zakończ")

    opcja = int(input("podaj wybór: " ))

    if opcja == 1:

        uczestnik = pobierz_uczestnika()
        if uczestnik in warsztat_python:
            print("Ta osoba jest już zapisana na ten warsztat")
        else:
            warsztat_python.add(uczestnik)
            print("Dodano uczestnika!")

    if opcja == 2:
        uczestnik = pobierz_uczestnika()
        if uczestnik in warsztat_ai:
            print("Ta osoba jest już zapisana na ten warsztat")
        else:
            warsztat_ai.add(uczestnik)
            print("Dodano uczestnika!")

    if opcja == 3:
        print("Uczestnicy warsztatów Python:")

        for imie, nazwisko in warsztat_python:
            print(f"  {imie} {nazwisko}")

        print("\n--- Uczestnicy warsztatów AI ---")

        for imie, nazwisko in warsztat_ai:
            print(f"{imie} {nazwisko}")

    if opcja == 4:
        oba = warsztat_python & warsztat_ai
        print(f"wszyscy uczestnicy:")
        for imie, nazwisko in oba:
            print(f"{imie} {nazwisko}")

    if opcja == 5:
        unikalni = warsztat_ai | warsztat_python
        print(f"Wszyscy unikalni uczestnicy: \n{unikalni}")

    if opcja == 0:
        print("Zakończono")
        break

