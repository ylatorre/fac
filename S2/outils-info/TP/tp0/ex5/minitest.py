
from qtido import *

f = creer(800, 600, True)
mark = 5

r = 150
s = 50

couleur(f, 0.2, 0.2, 0.2)
ligne(f, 400 - r, 300, 400 + r, 300)
ligne(f, 400, 300 - r, 400, 300 + r)

couleur(f, 0, 1, 1)
cercle(f, 400, 300, r)

couleur(f, 1, 1, 0)
texte_centre(f, 400, 300+s/2, s, "Centre")
cercle(f, 400, 300+s/2, mark)

couleur(f, 1, .5, .5)
texte(f, 400+r, 300+s/2, s, "Gauche")
cercle(f, 400+r, 300+s/2, mark)

couleur(f, 1, 0, 0)
ligne(f, 0, 300 + s/2, 800, 300 + s/2)
texte(f, 10, 300+s/2, 8, "ligne du bas")
cercle(f, 10, 300+s/2, mark)

attendre_fermeture(f)
