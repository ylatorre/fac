n = int(input("valeur de n: "))


acc = 0
for element in range(1, n + 1):
    acc = acc + n / (n + 1)

print(acc)