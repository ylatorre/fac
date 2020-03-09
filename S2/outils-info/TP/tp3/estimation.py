import random
import math
liste = input('n et r : ').split()
n = float(liste[0])
r = float(liste[1])
print(n, r)
for i in range(int(n)):
    x = random.random()
    y = random.uniform(-r, r)
    xcal = x * 2 - 1
    print('test', n, x, xcal,y)


N=1000000
m = 0
    
        
for i in range(0,N):
    y = random.random()
    x = random.random()
    if (x**2+y**2)<=1:
        m = m + 1
print('estimation de pi a',4*m / N)

