x = int(input("podaj cene produktu:"))

y = int(input("podaj liczbe sztuk:"))

wartosc = x*y
if wartosc > 100:
    koszt_dostawy = 0
 
print("wartośc produktów:", wartosc)
print("koszt dostawy:", koszt_dostawy)
print("do zapłaty:", wartosc+koszt_dostawy)