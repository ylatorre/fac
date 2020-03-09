from random import randint, uniform

n = int(input("Valeur Nombre : "))
if n % 2 == 0:
    notes = []
    coef = []
    sommenum = 0
    sommecoef = 0
    for i in range(n):
        notes.append(uniform(0, 20))
        coef.append(randint(1, 4))
        print(i + 1, "Une note de", notes[i], "avec un coefficient de", coef[i])
        sommenum = sommenum + notes[i] * coef[i]
        sommecoef = sommecoef + coef[i]
    moypond = sommenum / sommecoef
    print('La moyenne pondere est :', moypond)
else:
    print('Erreur vueillez reassayer')