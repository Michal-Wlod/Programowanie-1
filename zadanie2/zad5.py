haslo = "Python123"
liczba_prob = 3
while liczba_prob > 0:
    x = str(input("podaj haslo: "))
    liczba_prob -= 1
    if x == haslo:
        print("Logowanie udane")
        break
    else:
        print(f"Pozostałe próby {liczba_prob}")
    if  liczba_prob == 0:
        print("Konto zablokowane")
        break
