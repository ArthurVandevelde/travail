#Exercice2
def quatreOperations(a, b):
    adition = a + b
    soustraction = a - b
    multiplication = a * b
    division = a / b
    return adition, soustraction, multiplication, division

#exercice3

def prefixe (e,t):
    nouveau_tuple = e, + t
    return nouveau_tuple

def sufixe (e,t):
    nouveau_tuple = t + e,
    return nouveau_tuple

def inseve (e,i,t):
    nouveau_tuple = t[0:i] + e, + t[i+len(t)]
    
#exercice4
    

def supprime (i,t):
    nouveau_tuple = t[0:i] + t[i+1:len(t)]
    return nouveau_tuple

#exerce5
def ajoute(t1,t2):
    t = ()
    for i in range(len(t1)):
        t = (t1[i] + t2[i],) + t
    return t
