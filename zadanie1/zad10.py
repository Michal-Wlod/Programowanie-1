x = int(input("podaj liczbę studentów:"))
if x <= 0:
    print("nieprawidłowe dane")
    x = int(input("podaj liczbę studentów:"))

def wyliczenie_oceny(liczba_p):
    if liczba_p >= 90:
        return 5
    elif liczba_p >= 80:
        return 4.5
    elif liczba_p >= 70:
        return 4
    elif liczba_p >= 60:
        return 3.5
    elif liczba_p >= 50:
        return 3
    else:
        return 2

for i in range(x):
    nazwisko = str(input("podaj nazwisko studenta:"))
    liczba_p = int(input("podaj liczbę punktów:"))
    if liczba_p < 0 or liczba_p > 100:
        print("nieprawidłowa liczba punktów")
        liczba_p = int(input("podaj liczbę punktów:"))
    w_o = wyliczenie_oceny(liczba_p)
    
    print("Nazwisko:", nazwisko , "- Liczba punktów:", liczba_p, "- Ocena:", w_o)