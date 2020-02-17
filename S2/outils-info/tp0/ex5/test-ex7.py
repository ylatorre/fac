
from qtido import *

f = creer(800, 600)
x = 400
y = 100
r = 10
more = ""

ajouter_zone_texte(f, "txt1", 50, 50, 250, 270)
changer_champ_texte(f, "txt1", "Click @ {click}\nReClick @ {click}")

txt = ""
stroke = 1
while not est_fermee(f):
    effacer(f)
    couleur(f, 1, 1, 0.5)
    disque(f, x, y, r)

    couleur(f, 1,1,0)
    cadre(f, 40, 40, 260, 280)
    texte_centre(f, 400, 300, 25, txt.replace('{click}', more))

    attendre_evenement(f, 10)
    e = dernier_evenement(f)
    if e == 16777216: # Touche ECHAP
        supprime_widgets(f)
        import random
        ajouter_zone_texte(f, "txt1", random.randint(60,100), 50, 250, 70)
        changer_zone_texte(f, "txt1", "Hello")
        stroke += 1
        epaisseur_du_trait(f, stroke)
    elif e == "txt1":
        txt = lire_zone_texte(f, "txt1")
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
