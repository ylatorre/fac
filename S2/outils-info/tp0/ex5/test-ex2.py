
from qtido import *
import sys

f = creer(800, 600)
x = 400
y = 100
r = 10

ajouter_bouton(f, "Bouton1", 50, 50, 250, 70, "Ping")

while not est_fermee(f):
    effacer(f)
    couleur(f, 1, 0.5, 0.5)
    cercle(f, x, y, r)

    couleur(f, 1,1,0)
    cadre(f, 40, 40, 260, 80)

    attendre_evenement(f, 10)
    if dernier_evenement(f) is not None:
        e = dernier_evenement(f)
        print(e)
        if e == 16777216: # Touche ECHAP
            sys.exit()
        elif e == "Bouton1":
            r = 1
    else:
        r = r + 0.3
        if r > 50:
            r = 1
