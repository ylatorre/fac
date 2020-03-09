# 1) imports
import math

# 2) définitions de fonctions


def input_liste_nombres():
    entrees = input_liste("Nombres (séparés par des espaces) : ", " ")
    valeurs = en_float(entrees)
    return valeurs

    
# 3 et 4) programme principal
nbrs = input_liste_nombres()
carres = au_carre(nbrs)
afficher_liste_multiligne(carres)
