
x = int(input("kwota dodawana co tydzień:"))
if x <= 0:
    print("nieprawidłowe dane")
    x = int(input("kwota dodawana co tydzień:"))
czas = int(input("liczba tygodni:"))
if czas <= 0:
    print("nieprawidłowe dane")
    czas = int(input("liczba tygodni:"))
oszczednosci = 0

for i in range(czas):
    oszczednosci += x
    print("tydzień:", i+1, "oszczędności:", oszczednosci)
print("Łączne oszczędności po", czas, "tygodniach:", oszczednosci)