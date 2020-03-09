entree = input('Entrer Valeur :')
parties = entree.split(' ')
nbre = len(parties)
print("il y a", nbre, "parties.")

n = 0
for i in parties:
    print('  - partie',n,":",i)
    n = n + 1