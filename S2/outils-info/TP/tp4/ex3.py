
from qtido import *




# ligne(f,x1,y1,x2,y2)
# triangle = ligne
def triangle(f,x1,y1,x2,y2,x3,y3):
    ligne(f,x1,y1,x2,y2)
    ligne(f,x1,y1,x3,y3)
    ligne(f,x3,y3,x2,y2)
    # ligne(f,x2,y3,x1,y3)

    
# NE RIEN MODIFIER EN DESSOUS DE CETTE LIGNE
f = creer(800, 400)

triangle(f, 50, 50, 750, 50,   50 , 350)
triangle(f, 50, 50, 750, 50,   70 , 350)
triangle(f, 50, 50, 750, 50,   90 , 350)
triangle(f, 50, 50, 750, 50,  110 , 350)
triangle(f, 50, 50, 750, 50,  130 , 350)
triangle(f, 50, 50, 750, 50,  150 , 350)
couleur(f, 1, 0, 0)
triangle(f, 50, 50, 750, 50,  170 , 350)
triangle(f, 50, 50, 750, 50,  190 , 350)
triangle(f, 50, 50, 750, 50,  210 , 350)
triangle(f, 50, 50, 750, 50,  230 , 350)
triangle(f, 50, 50, 750, 50,  250 , 350)
triangle(f, 50, 50, 750, 50,  270 , 350)
couleur(f, 0, 1, 0)
triangle(f, 50, 50, 750, 50,  290 , 350)
triangle(f, 50, 50, 750, 50,  310 , 350)
triangle(f, 50, 50, 750, 50,  330 , 350)
triangle(f, 50, 50, 750, 50,  350 , 350)
triangle(f, 50, 50, 750, 50,  370 , 350)
triangle(f, 50, 50, 750, 50,  390 , 350)
couleur(f, 0, 0, 1)
triangle(f, 50, 50, 750, 50,  410 , 350)
triangle(f, 50, 50, 750, 50,  430 , 350)
triangle(f, 50, 50, 750, 50,  450 , 350)
triangle(f, 50, 50, 750, 50,  470 , 350)
triangle(f, 50, 50, 750, 50,  490 , 350)
triangle(f, 50, 50, 750, 50,  510 , 350)
couleur(f, 1, 1, 0)
triangle(f, 50, 50, 750, 50,  530 , 350)
triangle(f, 50, 50, 750, 50,  550 , 350)
triangle(f, 50, 50, 750, 50,  570 , 350)
triangle(f, 50, 50, 750, 50,  590 , 350)
triangle(f, 50, 50, 750, 50,  610 , 350)
triangle(f, 50, 50, 750, 50,  630 , 350)
couleur(f, 1, 0, 1)
triangle(f, 50, 50, 750, 50,  650 , 350)
triangle(f, 50, 50, 750, 50,  670 , 350)
triangle(f, 50, 50, 750, 50,  690 , 350)
triangle(f, 50, 50, 750, 50,  710 , 350)
triangle(f, 50, 50, 750, 50,  730 , 350)
resultat = triangle(f, 50, 50, 750, 50,  750 , 350)

exporter_image(f, "triangles.png")

if resultat is not None:
    print("ERREUR: triangle ne doit pas renvoyer de valeur")
    exit()

attendre_fermeture(f)

