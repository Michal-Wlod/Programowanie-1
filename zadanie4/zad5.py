
def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def pomnoz(a, b):
    return a * b

def dziel(a, b):
    if b == 0:
        return "Błąd: Nie można dzielić przez zero!"
    return a / b

def poteguj(a, b):
    return a ** b

def srednia(lista_liczb):
    return sum(lista_liczb) / len(lista_liczb)

def wyswietl_menu():
    print("\n--- KALKULATOR ---")
    print("1 – dodawanie")
    print("2 – odejmowanie")
    print("3 – mnożenie")
    print("4 – dzielenie")
    print("5 – potęgowanie")
    print("6 – średnia")
    print("0 – zakończ")

def main():
    while True:
        wyswietl_menu()
        opcja = int(input("Wybierz opcję: "))

        if opcja == 0:
            print("Koniec programu.")
            break

        if opcja in [1, 2, 3, 4, 5]:
            a = float(input("Podaj pierwszą liczbę: "))
            b = float(input("Podaj drugą liczbę: "))

            if opcja == 1:
                print("Wynik:", dodaj(a, b))
            elif opcja == 2:
                print("Wynik:", odejmij(a, b))
            elif opcja == 3:
                print("Wynik:", pomnoz(a, b))
            elif opcja == 4:
                print("Wynik:", dziel(a, b))
            elif opcja == 5:
                print("Wynik:", poteguj(a, b))

        elif opcja == 6:
            wprowadzony_tekst = input("Podaj liczby rozdzielone spacją: ")
            liczby = [float(x) for x in wprowadzony_tekst.split()]
            print("Średnia wynosii:", srednia(liczby))

        else:
            print("Nieprawidłowy wybór!")

if __name__ == "__main__":
    main()