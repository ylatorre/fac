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
    print('delta :',d,'\nracine 1:',r1,'\nracine 2:',r2)
else:
    if d == 0 and a != 0:
        r3 = int((-b/(2*a)))
        print(r3)
    else:
        if d <= 0:
            print('erreur')


