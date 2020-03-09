# Ex 1:
# 1)
qui = 'Robin'
print('Bonjour',qui,'!')
# 2)
qui = 'Robin'
print('Bonjour ',qui,'!',sep="")
# 3)
qui = input('Entrez votre nom :')
print('Bonjour',qui,'!')
# 4)
qui = input('Entrez votre nom :')
jour = input('Quel jour de la semaine on est ? ')
print('Bonjour',qui,',je te souhaites un bon',jour)
# 6)
nb1 = 27
nb2 = 5
calcule = nb1 % nb2
print('Le reste de la division',nb1,'/',nb2,'est',calcule)

# 7)
nb1 = int(input('entier a:'))
nb2 = int(input('entier b:'))
calcule = nb1 % nb2
print('Le reste de la division',nb1,'/',nb2,'est',calcule)

# Ex 2:
# 8)
import math 

r1 = 0
r2 = 0

a = int(input('a :'))
b = int(input('b :'))
c = int(input('c :'))

d = int(pow(b,2)+4*a*b)
if a == 0:
    print("c'est pas une fonction du second degres !!!!")
        
if d > 0 and a != 0:
    r1 = int((b-math.sqrt(d))/(2*a))
    r2 = int((b+math.sqrt(d))/(2*a))
    print('nombre de racine 2')
    print('delta :',d,'\nracine 1:',r1,'\nracine 2:',r2)
else:
    if d == 0 and a != 0:
        r3 = int((-b/(2*a)))
        print('Nombre de racine 1')
        print('delta :',d,'\nracine 1:',r3)

        print(r3)
    else:
        if d <= 0:
            print('erreur')

# Ex 3:
# 12)
  






