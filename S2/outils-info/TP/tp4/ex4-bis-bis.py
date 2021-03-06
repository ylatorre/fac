# coding=<utf-8>
# 1) imports
from qtido import *

# 2) définitions de fonctions
f = creer(1000,1000)

def carre(fen,x,y,taille):
    rectangle(fen,x,y,x+taille,y+taille)
# carre(f,100,100,100)
# carre(f,400,100,100)
# carre(f,250,250,100)
# carre(f,450,450,100)
# carre(f,150,650,200)
# (f,x,y,taille)


def cube(fen,x,y,taille):
    cadre(fen,x,y,x+taille,y+taille)
    # ligne(fen,x,y,x2,y2)
    # ligne(fen,x2,y2,x3,y3)
    # cadre(fen,x2,y2,x+taille,y+taille)
#cube(f,x,y,taille,x2,y2,x3,y3)
cube(f,200,250,100)
cube(f,270,200,100)

def line(fen,x,y,x2,y2,r,g,b):
    ligne(fen,x,y,x2,y2)
    couleur(f,r,g,b)
line(f,200,250,270,200,1,1,0)
line(f,300,250,370,200,0,0,1)
line(f,370,300,300,350,0,1,0)
line(f,270,200,200,250,0,1,1)
line(f,200,350,270,300,1,0,1)


# cube(f,450,100,100,100,200)
# cube(f,250,250,100,100,200)


exporter_image(f, "triangles.png")
exporter_image(f,"refr.png")
attendre_pendant(f,25000)
# attendre_fermeture(f)


### NE PAS MODIFIER CETTE FONCTION ###
def verifie_presque_egal(a, b):
    if round(a, 5) != round(b, 5):
        raise ValueError("ERREUR : «"+str(a)+"» != «"+str(b)+"»")
######################################



    
# 3 et 4) programme principal

### Dé-commenter les tests suivants, petit à petit
### au fur et à mesure que vous écrivez les fonctions

#verifie_presque_egal( carre(8), 64)
#verifie_presque_egal( carre(-10), 100)
#verifie_presque_egal( cube(10), 1000)
#verifie_presque_egal( cube(-0.1), -0.001)
#verifie_presque_egal( logbase(1024, 2), 10)
#verifie_presque_egal( logbase(1024, 1024), 1)
#verifie_presque_egal( aire_disque(2.5), 19.634954084936208)
#verifie_presque_egal( volume_cylindre(2.5, 100), 1963.4954084936208)

### Ajouter vos propres tests ci-dessous


