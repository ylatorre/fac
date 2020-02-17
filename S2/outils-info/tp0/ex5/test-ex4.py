
from qtido import *
import sys

f = creer(800, 600)

ajouter_slider(f, "rayon", 50, 20, 500, 40, 1, 200)
ajouter_slider(f, "r", 50, 50, 500, 70, 0, 255)
ajouter_slider(f, "g", 50, 70, 500, 90, 0, 255)
ajouter_slider(f, "b", 50, 90, 500,110, 0, 255)
ajouter_slider(f, "a", 50,120, 500,140, 0, 255)
changer_slider(f, "rayon", 50)
changer_slider(f, "r", 120)
changer_slider(f, "a", 255)

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
    
    radius = lire_slider(f, "rayon")
    r = lire_slider(f, "r")/255
    g = lire_slider(f, "g")/255
    b = lire_slider(f, "b")/255
    a = lire_slider(f, "a")/255
    couleur(f, r, g, b, a)
    disque(f, 400, 300, radius)

    couleur(f, 1, 1, 1, .7)
    texte(f, 520, 35, 14, "r = "+str(radius))
    texte(f, 520, 65, 14, "R = "+str(r))
    texte(f, 520, 85, 14, "G = "+str(g))
    texte(f, 520, 105, 14, "B = "+str(b))
    texte(f, 520, 135, 14, "A = "+str(a))


    attendre_evenement(f, 10)
    e = dernier_evenement(f)
    if e == 16777216: # Touche ECHAP
        sys.exit()
