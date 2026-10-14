x = int(input("podaj wiek:"))

if x < 13:
    print("Wypożyczanie niemożliwe")
    exit()


if x > 18:
    odpowiedz_2 = str(input("Czy masz dokument tozsamosci? (tak/nie)"))
    if odpowiedz_2 == "tak":
        print("Wypożyczanie możliwe")
        exit()
    else:
        print("Wypożyczanie niemożliwe")
        exit()

if x < 18 and x >= 13:
     odpowiedz_1 = str(input("Czy masz zgode opiekuna? (tak/nie)"))
     if odpowiedz_1 == "tak":
         odpowiedz_2 = str(input("Czy masz dokument tozsamosci? (tak/nie)"))
         if odpowiedz_2 == "tak":
             print("Wypożyczanie możliwe")
             exit()
         else:
             print("Wypożyczanie niemożliwe")
             exit()
     else:
         print("Wypożyczanie niemożliwe")
         exit()
else:
     print("Wypożyczanie niemożliwe")
     exit()
