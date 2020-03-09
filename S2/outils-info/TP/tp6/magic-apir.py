from qtido import *
import sys

f = creer(600,600)
t = creer_tortue(f)
def spirt(x):
    j = 30
    l = 0
    for i in range(x):
        j = j + 10
        tortue_gauche(t,l)
        tortue_avance(t,30+j)
        l = 90




spirt(int(sys.argv[1]))

attendre_fermeture(f)