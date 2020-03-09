annee = int(input('annee de depart :'))
anneeF = int(input('annee de Fin :'))
bixe = annee % 4
bixe2 = annee % 400
nonbixe = annee % 100
i = anneeF
while annee != anneeF + 1:
    if bixe == 0 and (nonbixe != 0 or bixe2 == 0 ):
        print(annee,'annee bissextile')
    else:
        if bixe != 0 and (nonbixe == 0 or bixe2 != 0) :
            print(annee,'annee normal')   
    annee = annee + 1
    i = i - 1
    bixe = annee % 4
    bixe2 = annee % 400
    nonbixe = annee % 100