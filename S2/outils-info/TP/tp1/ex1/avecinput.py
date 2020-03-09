p = int(input('enter valeur de p :'))
q = int(input('enter valeur de q :'))
somme = p + q

print("p vaut ",p," et q vaut ",q,", leur somme vaut ",somme)

if int(p) %  int(q) == 0 :
    print("Multiple")
else:
    print("Pas multiple")




tmp = int(p)
p = int(q)
q = tmp

print("La nouvelle valeur de p est :",p)
print("La nouvelle valeur de q est :",q)

somme2 = p + q

print("La somme des nouvelles variables p et q vaut ",somme2)