x = input("podaj liczbę studentów: ")

punkty = []

for i in range(int(x)):
    l_p = int(input(f"podaj liczbę punktów studenta {i+1}: "))
    if l_p < 0 and l_p > 100:
        print("podano nieprawidłową wartość! od 0 do 100")
        l_p = int(input(f"podaj liczbę punktów studenta {i+1}: "))

    punkty.append(l_p)

suma_p = sum(punkty)
średnia = suma_p/len(punkty)

print(średnia)
print(f"Najwyższy wynik: {max(punkty)}")
print(f"Najmniejszy wynik {min(punkty)}")
posortowane = sorted(punkty)
print(f"wyniki rosnąco: {posortowane}")

zaliczenia = 0
for i in posortowane:
    if i >= 50:
        zaliczenia += 1
print(f"Liczba zaliczeń: {zaliczenia}")

