liste_fruit = ['','banane', 'noix', 'myrtille','wrg','hreh']
nbFruit = len(liste_fruit)
print('Il y a', nbFruit, 'fruits')
i = 0
n = 0

# print("\n  -".join(liste_fruit))
while i == 0:
    if nbFruit > n:
        print('  -', liste_fruit[n])
        n = n + 1
        
    else:
        if nbFruit <= n:
            i = 1
    
        
    