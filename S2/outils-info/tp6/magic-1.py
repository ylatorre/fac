from qtido import *
import sys


def cercle_(r,e):
    f = creer(600,600)
    i = 0
    j = 0
    l = 0
    while i == 0:
        if r > j:
            l = l + 20
            couleur(f,0,0,1)
            cercle(f,300,300,l)
            j = j +1
        else:
            if r <= j:
                couleur(f,1,0,0)
                cercle(f,300,300,l+20)
                i = 1
    exporter_image(f,e)
    attendre_fermeture(f)
cercle_(int(sys.argv[1]),str(sys.argv[2]))