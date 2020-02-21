# 1) imports
import math

# 2) définitions de fonctions


### NE PAS MODIFIER CES FONCTIONS ###
def verifie_presque_egal_liste(a, b):
    if len(a) != len(b):
        raise ValueError("ERREUR len(...) : «"+str(a)+"» != «"+str(b)+"»")
    for i in range(len(a)):
        verifie_presque_egal(a[i], b[i])
def verifie_presque_egal(a, b):
    if round(a, 5) != round(b, 5):
        raise ValueError("ERREUR : «"+str(a)+"» != «"+str(b)+"»")
######################################


    
# 3 et 4) programme principal

### Dé-commenter les tests suivants, petit à petit
### au fur et à mesure que vous écrivez les fonctions

#l1 = [1, 10, 20]
#verifie_presque_egal_liste( au_carre(l1), [1, 100, 400])
#verifie_presque_egal_liste(  au_cube(l1), [1, 1000, 8000])
#lg = math.log
#verifie_presque_egal_liste( au_logbase(2, l1), [lg(1)/lg(2), lg(10)/lg(2), lg(20)/lg(2)])
#verifie_presque_egal( produit(l1), 200)
#verifie_presque_egal( somme(l1), 31)
#l2 = [ [1, 2, 3], [10, 20, 30] ]
#verifie_presque_egal( somme_2d(l2), 66)
#verifie_presque_egal( produit_2d(l2), 36000)

### Ajouter vos propres tests ci-dessous


