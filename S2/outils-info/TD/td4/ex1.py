
def au_carre(liste):
    x=[]
    for i in range(len(liste)):
        x.append(float(liste[i])**2)
    print(x)    
    return x
def au_logbase(b):
    j = []
    for i in range(len(b)):
        j.append(math.log10(float(b[i])))
    return j

def tousfloat(liste):
    l=[]
    for i in range(len(liste)):
        l.append(float(liste[i]))
    print(l)
tousfloat(['100','1.414','9','10.10','999'])
au_carre([10,1.414,9,10.10,'2'])

