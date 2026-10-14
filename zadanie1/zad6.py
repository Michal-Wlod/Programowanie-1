temp = int(input("podaj temperature:"))
obecnosc = str(input("czy ktos jest w domu? (tak/nie)"))
okno = str(input("czy okno jest otwarte? (tak/nie)"))

if okno == "tak":
    print("Ogrzewanie: wyłączone")
    print("Powód: okno jest otwarte")
    exit()
if obecnosc == "tak" and temp < 20 and okno == "nie":
        print("Ogrzewanie: włączone")
        print("Powód: temperatura jest niższa niż 20 stopni i ktoś jest w domu")
        exit()
if obecnosc == "nie" and temp < 16 and okno == "nie":
        print("Ogrzewanie: włączone")
        print("Powód: temperatura jest niższa niż 16 stopni")
        exit()
else:
    print("Ogrzewanie: wyłączone")