n = int(input("valeur de n: "))

j = 0
acc = 1
for element in range(1, n + 1):
    if j == 0:
        acc = acc - n 
        j = 1
    else:
        if j == 1:
            j = 0
            acc = acc + n 

print(acc)