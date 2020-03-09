def input_liste_nombres():
    entrees = input_liste("Nombres (séparés par des espaces) : ", " ")
    valeurs = en_float(entrees)
    return valeurs


def input_liste(nbrs,val):
    val = input(nbrs)
    nbrs2 = val.split()
    return nbrs2
            
            
def en_float(entrees): 
    j = []
    for i in range(len(entrees)):
        if int != entrees[i] or float != entrees[i]:
            j.append(float(entrees[i]))
    return j           
            
            
def au_carre(valeurs):
    x=[]
    for i in range(len(valeurs)):
        x.append(valeurs[i]**2)
    return x


def afficher_liste_multiligne(val):
    z = 0
    for i in range(len(val)):
        print(i+1,'-',val[i])
        z = val[i] + z
    print("Total :",z)


def init():
    nbrs = input_liste_nombres()
    carres = au_carre(nbrs)
    return carres


afficher_liste_multiligne(init())
