
from qtido import *

f = creer(800, 600)
x = 400
y = 100
r = 10
more = ""

ajouter_champ_texte(f, "txt1", 50, 50, 250, 70)
changer_champ_texte(f, "txt1", "Click @ ")

txt = ""
while not est_fermee(f):
    effacer(f)
    couleur(f, 1, 1, 0.5)
    disque(f, x, y, r)

    couleur(f, 1,1,0)
    cadre(f, 40, 40, 260, 80)
    texte_centre(f, 400, 300, 25, txt+more)

    attendre_evenement(f, 10)
    e = dernier_evenement(f)
    if e == 16777216: # Touche ECHAP
        supprime_widgets(f)
        import random
        ajouter_champ_texte(f, "txt1", random.randint(60,100), 50, 250, 70)
        changer_champ_texte(f, "txt1", "Hello")
    elif e == "txt1":
        txt = lire_champ_texte(f, "txt1")
    elif est_souris(f, e, "PRESS"):
        _,x,y,b = e
        r = 20
    elif est_souris(f, e, "MOVE"):
        _,x,y = e
        r = r - 0.5
        if r < 10: r = 20
    elif est_souris(f, e, "RELEASE"):
        _,x,y,b = e
        r = 10
    more = str(x)+" "+str(y)
