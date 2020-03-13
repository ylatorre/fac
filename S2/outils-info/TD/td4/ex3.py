
def au_carre(liste):

    x=[]
    for i in range(len(liste)):
        x.append(float(liste[i])**2)
    return x
def au_log(b):
    j = []
    for i in range(len(b)):
        j.append(math.log10(float(b[i])))
    return j

def tousfloat(liste):
    l=[]
    for i in range(len(liste)):
        l.append(float(liste[i]))
    return l

def liste_floats():
    w = input("enter valeur :\n").split()
    return w

def tous_sauf_un(liste):
    l = []
    for i in range(1,len(liste)):
        l.append(liste[i])
    return l

def un_sur_deux(liste):
    l = []
    for i in range(0,len(liste),2):
        l.append(liste[i])
    return l

def principal():
    l =['tous_sauf_un','un_sur_deux','tousfloat','au_carre','au_log']
    l2 =[tous_sauf_un,un_sur_deux,tousfloat,au_carre,au_log]

    r = liste_floats()
    
    for i in range(len(l)):
        if r[0]==l[i]:
            j = l2[i](tous_sauf_un(r))
            print(j)
principal()