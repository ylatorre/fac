# outils pour cellules.py

from qtido import *

def liste_de_zeros(largeur):
    res = []
    for x in range(largeur):
        res.append(0)
    return res
    
def que_des_zeros(hauteur, largeur):
    res = []
    for y in range(hauteur):
        res.append(liste_de_zeros(largeur))
    return res
    
def afficher_grille(f, grille):
    couleur(f, 1, 1, 0)
    for y in range(len(grille)):
        ligne = grille[y]
        for x in range(len(ligne)):
            valeur = ligne[x]
            if valeur >= 1:
                disque(f, x*20 + 10, y*20 + 10, 10)

def init_boucle_deux_iterations(gr):
    gr[10][5] = gr[10][6] = gr[10][7] = 1

def init_stable(gr):
    gr[5][5] = gr[5][6] = gr[4][5] = gr[4][6] = 1

def init_devient_stable_en_trois(gr):
    gr[10][10] = gr[10][11] = gr[10][12] = gr[9][12] = 1

def init_se_deplace_jusquau_bord(gr):
    gr[3][10] = gr[3][11] = gr[3][12] = gr[2][12] = gr[1][9] = 1

def init_kaboom(gr):
    init_boucle_deux_iterations(gr)
    gr[3][2] = gr[3][3] = gr[3][4] = gr[2][4] = gr[1][1] = 1


