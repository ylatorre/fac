
from qtido import *
import sys

f = creer(800, 600)
x = 400
y = 100
r = 10

while not est_fermee(f):
    effacer(f)
    couleur(f, 1, 0.5, 0.5)
    cercle(f, x, y, r)

    attendre_evenement(f, 10)
    if dernier_evenement(f) is not None:
        e = dernier_evenement(f)
        print(e)
        if e == 16777216: # Touche ECHAP
            sys.exit()
    else:
        r = r + 1
        if r > 50:
            r = 1
