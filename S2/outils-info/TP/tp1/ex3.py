import time
from random import *

liste = ['oiseau', 'moustique', 'chat', 'chien', 'tyrannosaure', 'pterodactyle'] #Liste des elements de l'exercice 
listeNom = ["sabrina", 'quentin', 'yvan','chocolatine']#, 'tacos'] nom pour identifiant 
listeFuck = ['tu te fou de ma ********','Encore heureux','Va te faire F*******','En plus tu me prend pour un Con, allez casse toi, me parle plus','Your talking to me'] 
listeYes = ['je suis un genie', 'tu trouvera personne qui fait mieux', 'Pffff trop simple','Booooommm respecte moi !!!!!',"Fuck Yeah"] 

p = 0
b = 1 
a = 0
i = 0
c = '0'
e = '(oui/non)'
rdm = randint(0, 4)
l = 0
d = ''

# w = 0
# def FoncNom(d):
print(" ".join(listeNom))
d = input("Qui es tu ?\n")
while l == 0 :
    if listeNom[0] == d:
        print('Pause')
        i = 1
        l = 1
        # return i
    else :
        if listeNom[1] == d:
            i = 0
            d = input('arret de mentir il est tous le temps en retard qui es tu reellement ?\n')
            # return d,i
        else:
            if listeNom[2] == d:
                t = input('tu veux du the ?\n')
                l = 1
                if t == 'oui':
                    print('tiens sert toi')
            else:
                if listeNom[3] == d:
                    print("Yes t'es le meilleur")
                    l = 1
                else:
                    if d != listeNom :
                        # print(listeFuck[rdm])
                        i = 0
                        d = input('access denied !!!!!!\n')
                     
                    # if listeNom[4] == d:
                    #     print("La commander est en cours d'execution veuiller patienter")
                    #     tacAdress = input("Adresse")
                    #     prix = input('Payer 10 000$(oui/non)')
                    #     if prix == 'oui':
                    #         time.sleep(5)
                    #         print("la commande a etais envoyer a",tacAdress,'au prix de 10 000$')
                    #         l = 1
                        
                           
         



            
# Programme qui corresponds a l'exercice 3 

while i == 0:
    print("c'est un ", liste[a],e)
    b = input('?')
    if b == 'oui' and a <= 5:
        i = 1
        print(listeYes[rdm])
    else :
        i = 0
        a= a + 1
        if a > 5 :
            print(listeFuck[0], e)
            c = input('?')
            if c == 'non' :
                print(listeFuck[1])
                i = 1
            
            else :
                print(listeFuck[2])
            i = 1


                            