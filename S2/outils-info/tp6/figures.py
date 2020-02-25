
from qtido import *


def principale(x,y):
    f = creer(800, 600); 
    cercle(f, 100, 300, 50)
    couleur(f, 1, 1, 0)
    disque(f, 200, 200, 50)
    couleur(f, 0, 1, 0)
    ligne(f, 400, 200, 450, 250)
    cadre(f, 500, 200, 550, 250)
    rectangle(f, 450, 250, 500, 300)
    losange(f,x,y)
    losange(f,x+100,y+200)
    losange(f,x+300,y+100)
    
    exporter_image(f, "question-losange.png")
    attendre_fermeture(f)


def losange(f,x,y):
    # f = creer(800,600)  
    couleur(f,1,0,0)
    ligne(f,x/4,y,x*1.75,y)
    ligne(f,x,y/2,x,y*1.5)
    ligne(f,x/4,y,x,y*1.5)
    ligne(f,x/4,y,x,y/2)
    ligne(f,x,y/2,x*1.75,y)
    ligne(f,x,y*1.5,x*1.75,y)
    
    # exporter_image(f, "question-losange.png")
    # attendre_fermeture(f)
    
    
# losange(principale(),400,300) 
# losange(principale(),200,400)   

principale(100,200)
# principale(500,200)

