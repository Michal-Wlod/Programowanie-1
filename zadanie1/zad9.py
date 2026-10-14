x = int(input("pierwsza liczba:"))
y = int(input("ostatnia liczba:"))
ilosc_parzystych = 0
for i in range(x, y + 1):
    if i % 2 == 0:
        print(i, "parzysta")
        ilosc_parzystych += 1
    else:
        print(i, "nieparzysta")

print("Liczba liczb parzystych:", ilosc_parzystych)