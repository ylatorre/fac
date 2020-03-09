


var1 = 10
var2 = 1.5
var3 = 2
var4 = 2.5

def produit(a,b):
    print("Appel de la fonction produit",a*b)


def somme(a,b):
    print("Appel de la fonction somme",a+b)



print("Programme principal")

somme(int(input("a")),int(input("b")))
produit(int(input("a")),int(input("b")))
somme(var1,var2)
somme(var3,var4)
produit(var1,var2)
produit(var3,var4)
