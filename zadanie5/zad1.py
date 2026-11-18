import numpy as np

pomiary = np.array([])
x = int(input("podaj liczbe pomiarów: "))
while x < 1:
    print("podano zła wartość.")
    x = int(input("podaj liczbe pomiarów: "))

for i in range(x):
    pomiar = int(input(f"podaj pomiar {i+1}: "))
    pomiary = np.append(pomiary, pomiar)

print(f"avg temp: {np.mean(pomiary)}")
print(f"min temp:{np.min(pomiary)}")
print(f"max temp:{np.max(pomiary)}")
print(f"rozstęp temp:{np.max(pomiary)-np.min(pomiary)}")