




def produit(a,b):
    print("Appel de la fonction produit",a*b)
    

def somme(a,b):
    print("Appel de la fonction somme",a+b)



liste = []
def calculer(nom):
    if nom[0] == "produit":
        print("multiplication de ")
        produit(float(nom[1]),float(nom[2]))
    else:
        print("addition de ")
        if "somme" == nom[0]:
            somme(float(nom[1]),float(nom[2]))

print("Programme principal")

print("somme")
somme(float(input("a :")),float(input("b :")))
print("poduit")
produit(float(input("a :")),float(input("b :")))
print("calculer")
calculer(nom = input("methode de calculer, a et b : ").split())