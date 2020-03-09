mul = int(input('valeur de mul : '))
limite = int(input('valeur de limite :'))
compte = 0
i = 1
while i <= limite:
    print(i)
    i = mul * i
    compte = compte + 1
print(compte)