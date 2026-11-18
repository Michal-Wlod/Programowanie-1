import pandas as pd
import matplotlib.pyplot as plt


def oblicz_ocene(punkty):
    if punkty < 50:
        return 2.0
    elif punkty < 60:
        return 3.0
    elif punkty < 70:
        return 3.5
    elif punkty < 80:
        return 4.0
    elif punkty < 90:
        return 4.5
    else:
        return 5.0


liczba_studentow = int(input("Podaj liczbe studentow: "))
while liczba_studentow < 1:
    print("Liczba studentow musi wynosic co najmniej 1.")
    liczba_studentow = int(input("Podaj liczbe studentow: "))

nazwiska = []
punkty_lista = []

for i in range(liczba_studentow):
    nazwisko = input("Nazwisko: ")
    punkty = float(input("Punkty: "))
    while punkty < 0 or punkty > 100:
        print("Liczba punktow musi byc w przedziale 0-100.")
        punkty = float(input("Punkty: "))
    nazwiska.append(nazwisko)
    punkty_lista.append(punkty)

df = pd.DataFrame({
    "Nazwisko": nazwiska,
    "Punkty": punkty_lista
})

df["Ocena"] = df["Punkty"].apply(oblicz_ocene)

print(df, sep="")
srednia = df["Ocena"].mean()
zaliczenia = (df["Ocena"] >= 3.0).sum()

print(f"Srednia ocen: {srednia}")
print(f"Liczba zaliczen: {zaliczenia}")

posortowane = df.sort_values("Punkty", ascending=False)
print("Posortowane wyniki (malejaco wg punktow):")
print(posortowane)

plt.bar(df["Nazwisko"], df["Ocena"])
plt.title("Wyniki egzaminu")
plt.xlabel("Student")
plt.ylabel("Ocena")
plt.ylim(0, 5.5)
plt.tight_layout()
plt.show()

df.plot(x="Nazwisko", y="Ocena", kind="bar", legend=False)
plt.title("Wyniki egzaminu")
plt.xlabel("Student")
plt.ylabel("Ocena")
plt.ylim(0, 5.5)
plt.tight_layout()
plt.show()