import matplotlib.pyplot as plt


def przelicz_ocene(pkt):
    if pkt < 50:
        return 2.0
    elif pkt < 60:
        return 3.0
    elif pkt < 70:
        return 3.5
    elif pkt < 80:
        return 4.0
    elif pkt < 90:
        return 4.5
    else:
        return 5.0


n = int(input("Podaj liczbę studentów: "))
nazwiska = []
punkty = []
oceny = []

for _ in range(n):
    nazwisko = input("Podaj nazwisko: ")
    pkt = float(input("Podaj punkty (0-100): "))
    oc = przelicz_ocene(pkt)

    nazwiska.append(nazwisko)
    punkty.append(pkt)
    oceny.append(oc)


srednia = sum(oceny) / len(oceny)
zliczeni_zdani = sum(1 for o in oceny if o >= 3.0)

print(f"\nŚrednia ocen: {srednia:.2f}")
print(f"Liczba osób z oceną co najmniej 3.0: {zliczeni_zdani}")

plt.bar(nazwiska, oceny)
plt.title("Oceny studentów")
plt.xlabel("Student")
plt.ylabel("Ocena")
plt.ylim(0, 5.5)
plt.show()