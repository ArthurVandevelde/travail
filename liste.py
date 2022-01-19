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
def enleveDoublon(liste):
    for doublon in liste:
        for doublon_v2 in range(liste):
            if doublon == doublon_v2 :
                del 
