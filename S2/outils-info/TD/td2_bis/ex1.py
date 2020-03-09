import math
x = input('x en cm : y en cm :').split()

print(x)

p = 0
d = float(math.sqrt(int(x[0])**2+int(x[1])**2))
n = 10
g = 100
print(d)


        
point = 10
for i in range(0,10, 2):
    if d <= i:
        print(point)
        break
    point = point - 2
    



    #     n = n - 1
    # else:
    #     if x < d:
    #         xCible = xCible + 1
    #         n = n - 1
    #     else:   
    #         if x == xCible and y == yCible:

    #             print("Le resultat est ", d)
    #             i = 1