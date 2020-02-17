
from qtido import *

f = creer(800, 600)
toto = True
tickness = 1
b = False

poly = []
while not est_fermee(f):
    effacer(f)

    couleur(f, 0.4, 0, 0)
    polygone(f, poly)

    couleur(f, 1, 1, 0.5)
    polyligne(f, poly)

    epaisseur_du_trait(f, tickness)

    attendre_evenement(f, 10)
    e = dernier_evenement(f)
    if e == 16777216: # Touche ECHAP
        if toto:
            toto = False
            poly = []
            fermer_fenetre(f)
            f = creer(800, 600)
        else:
            exit()
    elif est_souris(f, e, "PRESS"):
        _,x,y,_ = e
        poly.append([x,y])
        print(len(poly))
    elif est_souris(f, e, "MOVE"):
        _,x,y = e
        poly.append([x,y])
        print(len(poly))
    elif e == 66: # 'b' down
        print('NOW')
        b = True
    elif e == -66: # 'b' up
        b = False
    else: # simulation
        if 65 in les_touches_appuyees(f): # 'a' is pressed
            tickness += .2
            if tickness > 10:
                tickness = 1
        if b: # 'b' is pressed
            tickness -= .2
            if tickness < .1:
                tickness = 10
