
from qtido import *
import sys

f = creer(800, 600)

ajouter_slider(f, "tx", 50, 50, 500, 70, 0, 800)
ajouter_slider(f, "ty", 50, 70, 500, 90, 0, 600)
ajouter_slider(f, "10sx", 50, 90, 500,110, -100, 100)
ajouter_slider(f, "10sy", 50,120, 500,140, -100, 100)
ajouter_slider(f, "r", 50, 150, 500, 170, 0, 360)
changer_slider(f, "tx", 400)
changer_slider(f, "ty", 300)
changer_slider(f, "10sx", 10)
changer_slider(f, "10sy", 10)

while not est_fermee(f):
    effacer(f)
    couleur(f, 1, 1, 1)
    rectangle(f, 0, 300, 800, 600)

    couleur(f, 1/7, 1/7, 1/7)
    for x in range(50, 800, 100):
        rectangle(f, x, 0, x+50, 300)
    couleur(f, 6/7, 6/7, 6/7)
    for x in range(0, 800, 100):
        rectangle(f, x, 300, x+50, 600)

    tx = lire_slider(f, "tx")
    ty = lire_slider(f, "ty")
    sx = lire_slider(f, "10sx")/10
    sy = lire_slider(f, "10sy")/10
    r  = lire_slider(f, "r")
    
    utiliser_transformation(f, tx, ty)
    couleur(f, 1/3, 1/3, 1/3)
    rectangle(f, -30, -20, 30, 20)

    utiliser_transformation(f, tx, ty, sx, sy)
    couleur(f, 1, 0, 0, 0.5)
    rectangle(f, -30, -20, 30, 20)
    couleur(f, 1, 1, 0, 0.8)
    texte_centre(f, 0, 10, 20, "Go")

    utiliser_transformation(f, tx, ty, sx, sy, r)
    couleur(f, 0, 1, 0, 0.8)
    polygone(f, [[0, 0], [-10, -50], [10, -50]])
    texte_centre(f, 0, -50, 20, "Ok")

    annuler_transformation(f)
    couleur(f, 1, 1, 1, .7)
    texte(f, 520, 35, 14, "tx = "+str(tx))
    texte(f, 520, 65, 14, "ty = "+str(ty))
    texte(f, 520, 85, 14, "sx = "+str(sx))
    texte(f, 520, 105, 14, "sy = "+str(sy))

    attendre_evenement(f, 10)
    e = dernier_evenement(f)
    if e == 16777216: # Touche ECHAP
        sys.exit()
