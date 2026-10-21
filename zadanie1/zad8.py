x = int(input("wysokość choinki:"))

for i in range(x):
    print(" " * (x - i - 1) + "*" * (2 * i + 1))