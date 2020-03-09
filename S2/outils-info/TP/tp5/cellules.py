# 1) imports
from qtido import *
from outils import que_des_zeros, afficher_grille
from outils import init_boucle_deux_iterations, init_stable, init_devient_stable_en_trois, init_se_deplace_jusquau_bord

# 2) définitions de fonctions
def evolution(courant, H, L):
    # l'état suivant est VIDE pour l'instant
    suivant = que_des_zeros(H, L) # état suivant
    # on considère toutes les cases, sauf les bords (celà simplifie les choses)
    for y in range(1, H-1):
        for x in range(1, L-1):
            # règle simple et fausse
            if courant[y][x-1] > 0 or courant[y+1][x-1] > 0:
                suivant[y][x] = 0
    return suivant 1


# 3 et 4) programme principal

# état initial
H = 15
L = 20
f = creer(400, 300)
grille = que_des_zeros(H, L)

init_boucle_deux_iterations(grille)
#init_stable(grille)
#init_devient_stable_en_trois(grille)
#init_se_deplace_jusquau_bord(grille)

while not est_fermee(f):
    # affichage
    effacer(f)
    afficher_grille(f, grille)
    # événements
    attendre_evenement(f, 100)
    e = dernier_evenement(f)
    if e == 16777216: # touche ECHAP
        exit()
    elif e == 32: # touche ESPACE
        print("Évolution !")
        grille = evolution(grille, H, L)
