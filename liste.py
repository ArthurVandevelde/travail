#exercice2
##liste = ['Alice', 'Bob', 'Tom']
##
##liste.insert(2, "marc")
##print(liste)

#exercice3
##t = []
##for i in range(0,10,2):
##    t.append(i**2)


# exercice4
##t = [0]*10
##
##for i in range(len(t)):
##    t[i] = 10 - i


# 10 , 9 , 8 , 7 , 6, 5 , 4, 3 , 2 , 1

#exercice 5

liste_nom = ['Jean-Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien', 'Alexandre-Benoît', 'Louise']

def longueurNomV1(liste_nom) : 
    liste_longueur = []
    for nom in liste_nom:
        liste_longueur =liste_longueur + [len(nom)]
    print(liste_longueur)

def longueurNomV1_2(liste_nom) : 
    liste_longueur = []
    for nom in liste_nom:
        liste_longueur.append(nom)
    print(liste_longueur)

def longueurNomv2(liste_nom) : 
    liste_longueur = [0]*len(liste_nom)
    for i in range(len(liste_nom)):
        liste_longueur[i] = len(liste_nom[i])
    print(liste_longueur)
    
#exercice 6
t=['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']

def affiche_liste(liste):
    for c in liste:
        print(c,end='')

#exercice 7
    
liste = [23, 45, 23, 43, 7, 66, 21, 45, 23, 7, 200, 200]

                
def enleveDoublon(liste) : 
    liste_entier = []
    for nb in liste:
        if not(nb in liste_entier):
            liste_entier = liste_entier+[nb]
            # liste_entier.append(nb)
    print(liste_entier)

 # exercice 8

t1 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
t2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def alterne(t1,t2):
    liste=[]
    for i in range(len(t1)):
        liste = liste +([t1[i]] + [t2[i]])
    print(liste)
    
# exercice 9

a = [8468, 4560, 3941, 3328, 7, 9910, 9208, 8400, 6502, 1076, 5921, 6720, 948, 9561, 7391, 7745, 9007, 9707, 4370, 9636, 
     5265, 2638, 8919, 7814, 5142, 1060, 6971, 4065, 4629, 4490, 2480, 9180, 5623, 6600, 1764, 9846, 7605, 8271, 4681, 
     2818, 832, 5280, 3170, 8965, 4332, 3198, 9454, 2025, 2373, 4067]

b = [9093, 2559, 9664, 8075, 4525, 5847, 67, 8932, 5049, 5241, 5886, 1393, 9413, 8872, 2560, 4636, 9004, 7586, 1461, 350, 
     2627, 2187, 7778, 8933, 351, 7097, 356, 4110, 1393, 4864, 1088, 3904, 5623, 8040, 7273, 1114, 4394, 4108, 7123, 8001, 
     5715, 7215, 7460, 5829, 9513, 1256, 4052, 1585, 1608, 3941]

for i in range(len(a)):
    if a[i] == b[i]:
        print(a[i])
        print(i)
            
#exercice 9
            
#pas de fonction mais des boucle
#parcourir les liste, parcourir a ou bien b par indice

# exercice 10

liste = ["Bob", "Alice", "Marc", "Tom", "John"]

def permute(liste,i,j):
    """
    description: échange dans la liste les éléments d'indice i et j
    liste (list)
    i, j (int): indices des éléments à permuter 
    ATTENTION : MODIFICATION DE LA LISTE EN PLACE !!
    """
    c=liste[i]
    c2=[j]
    liste[i]=c2
    liste[j]=c
    return liste
