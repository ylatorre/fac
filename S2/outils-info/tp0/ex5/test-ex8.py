
from qtido import *
import sys

f = creer(800, 600)
x = 400
y = 100
r = 10

while not est_fermee(f):
    effacer(f)
    couleur(f, 1, 0.5, 0.5)
    disque(f, x, y, r)

    attendre_evenement(f, 1000)
    if dernier_evenement(f) is not None:
        e = dernier_evenement(f)
        print(e)
        if e == 16777216: # Touche ECHAP
            sys.exit()
        elif e == 32: # Touche Espace
            r = r + 5
        elif e == 65: # 'a'
            r = r + 5
            reinitialiser_attendre_evenement(f)
        elif e == 66: # 'b'
            r = r + 5
            reinitialiser_attendre_evenement(f, True)
            
        if r > 500:
            r = r - 500
    else:
        r = r - 50
        if r < 2:
            r = 500
