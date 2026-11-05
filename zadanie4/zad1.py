x = int(input("Podaj liczbe: "))
l_p = []
for i in range(x):
    pomiar = int(input(f"Pomiar {i+1}: "))
    l_p.append(pomiar)

print(f" pierwszy pomiar: {l_p[:1]}")
print(f" ostatni pomiar: {l_p[-1:]}")

if len(l_p) < 3:
    print(f"pomiary: {l_p}")
else:
    print(f" pierwsze 3 pomiary: {l_p[:3]}")
    print(f" ostatnie 3 pomiary: {l_p[-3:]}")

print(f"co drugi pomiar: {l_p[::2]}")
print(f"pomiary w odwrotnej kolejności {l_p[::-1]}")

l_p2 = l_p.copy()
l_p2[0] = 0
print(f"lista 1 = {l_p}")
print(f"lista 2 = {l_p2}")
