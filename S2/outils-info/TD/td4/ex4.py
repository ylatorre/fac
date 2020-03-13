from qtido import *
def principal():
    f = creer(250,250)
    for j in range(5):
        for i in range(5):
            if (i+j)%2 == 0:
                couleur(f,1,0,0)
            else:
                couleur(f,0,0,1)
            rectangle(f,i*50,j*50,i*50+50,j*50+50)

        while not est_fermee(f):
            attendre_evenement(f,100)
            e = dernier_evenement(f)
            if est_souris(f,e,"PRESS"):
                xy=coordonnees_souris(f,e)
                print("Click en x =",xy[0],"et y -",xy[1])
principal()