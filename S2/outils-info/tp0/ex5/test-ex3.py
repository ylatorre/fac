
from qtido import *
import sys

f = creer(800, 600)
x = 400
y = 100
r = 10

ajouter_champ_texte(f, "txt1", 50, 50, 250, 70)
changer_champ_texte(f, "txt1", "Hello")

txt = ""
while not est_fermee(f):
    effacer(f)
    couleur(f, 1, 0.5, 0.5)
    cercle(f, x, y, r)

    couleur(f, 1,1,0)
    cadre(f, 40, 40, 260, 80)
    texte_centre(f, 400, 300, 25, txt)

    attendre_evenement(f, 10)
    e = dernier_evenement(f)
    if e == 16777216: # Touche ECHAP
        sys.exit()
    elif e == "txt1":
        txt = lire_champ_texte(f, "txt1")
