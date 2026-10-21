temperatura = []

for i in range(7):
    temp = int(input("podaj temperature: "))
    temperatura.append(temp)
    i += 1

temp_avg = sum(temperatura) / len(temperatura)
pow_avg = []

for x in temperatura:
    if x > temp_avg:
        pow_avg.append(x)

print(f"Średnia temperatura:{round(temp_avg,1)}")
print(f"Najwyższa: {max(temperatura)}")

print(f"Najniższa: {min(temperatura)}")
print(f"temperatura powyżej średniej: {pow_avg}")
print(f"liczba dni: {len(pow_avg)}")