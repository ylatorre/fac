# 1) imports
import math

# 2) définitions de fonctions
def au_carre(liste):
    x=[]
    for i in range(len(liste)):
        x.append(float(liste[i])**2)
    return x
def au_cube(liste):
    x=[]
    for i in range(len(liste)):
        x.append(float(liste[i])**3)
    return x       

def au_logbase(v,b):
    j = []
    for i in range(len(b)):
        j.append(math.log10(float(b[i])) / math.log10(float(v)))
    return j

def somme(x):
    j = 0
    for i in range(len(x)):
        j = float(x[i]+j)
    return j

def produit(x):
    j = int(1)
    for i in range(len(x)):
        j = float(x[i]*j)
    return j


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

# au_carre([2,3,4,5])
# au_carre(input("entrer liste d'element pour obtenir le carre").split())
# au_cube([1,23,45,4,3])
# au_carre(input("entrer liste d'element pour obtenir le cube").split())


# 3 et 4) programme principal

### Dé-commenter les tests suivants, petit à petit
### au fur et à mesure que vous écrivez les fonctions
def somme_2d(x):
    y = []
    for i in range(len(x)):
        y = y + x[i]
    c = 0
    for i in range(len(y)):
        c = c + y[i]
    return c 

def produit_2d(x):
    y = []
    for i in range(len(x)):
        y = y + x[i]
    j = int(1)
    for i in range(len(y)):
        j = float(y[i]*j)
    return j

l1 = [1, 10, 20]
verifie_presque_egal_liste( au_carre(l1), [1, 100, 400])
verifie_presque_egal_liste( au_cube(l1), [1, 1000, 8000])
lg = math.log
verifie_presque_egal_liste( au_logbase(2, l1), [lg(1)/lg(2), lg(10)/lg(2), lg(20)/lg(2)])
verifie_presque_egal( somme(l1), 31)
verifie_presque_egal( produit(l1), 200)
l2 = [ [1, 2, 3], [10, 20, 30] ]
verifie_presque_egal( somme_2d(l2), 66)
verifie_presque_egal( produit_2d(l2), 36000)

### Ajouter vos propres tests ci-dessous


