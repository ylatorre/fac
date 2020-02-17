valeur = input('Entrer Valeur: ').split()
n = len(valeur)
i = 0
j = 0
print(valeur, n)
cal = 0
while i ==0:
    if n != j:
        cal = cal + float(valeur[j])
        j = j + 1
        print(cal)
    else:
        if n == j:
            print(cal / n)
            i = 1