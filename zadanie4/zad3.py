x = int(input("Podaj liczbe pomiarów: "))
l_p = []
print("max = 50")
for i in range(x):
    pomiar = int(input(f"Pomiar {i + 1}: "))
    l_p.append(pomiar)

l_p_w = [i for i in l_p if i > 50]
l_p_p = [i * 2 for i in l_p]
bomba = any(i>50 for i in l_p)
prawidlowe = all(i <= 50 for i in l_p)

print(l_p_w)
print(f"wartości pomnożone przez 2: {l_p_p}")
print(f"pomiary powyżej 50: {l_p_w}")
print(f"czy przekroczono 50: {'TAK' if bomba else 'NIE'}")
print(f"Czy wszystkie pomiary są prawidłowe: {'TAK' if prawidlowe else 'NIE'}")