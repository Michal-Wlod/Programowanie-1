x = int(input("podaj czas postoju:"))

if x <= 0:
    print("nieprawidłowe dane")
    x = int(input("podaj czas postoju:"))

if x <= 1:
    print("czas postoju:", x, "godzin")
    print("do zapłaty: 5zł")
if x > 1 and x <= 3:
    print("czas postoju:", x, "godzin")
    print("do zapłaty: 12zł")
if x > 3 and x <= 6:
    print("czas postoju:", x, "godzin")
    print("do zapłaty: 20zł")
if x > 6:
    print("czas postoju:", x, "godzin")
    print("do zapłaty: 30zł")
