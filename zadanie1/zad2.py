x = int(input("podaj liczbe punktów:"))

ocena = 0
if x >= 90:
    ocena = 5
elif x >= 80:
    ocena = 4.5
elif x >= 70:
    ocena = 4
elif x >= 60:
    ocena = 3.5
elif x >= 50:
    ocena = 3
else:
    ocena = 2 

print("liczba punktów:", x)
print("ocena:", ocena)