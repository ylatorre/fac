
from qtido import *


def principale():
    f = creer(800, 600);
    
    cercle(f, 100, 300, 50)
    couleur(f, 1, 1, 0)
    disque(f, 200, 200, 50)
    couleur(f, 0, 1, 0)
    ligne(f, 400, 200, 450, 250)
    cadre(f, 500, 200, 550, 250)
    rectangle(f, 450, 250, 500, 300)
    exporter_image(f, "salut.png")
    
    attendre_fermeture(f)



principale()

