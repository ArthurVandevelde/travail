from random import randrange
liste = []
for i in range(100):
    liste.append(randrange(500))

def recherche(liste, valeur):
    """
    Description de la fonction : Détermine si la valeur est présente dans la liste
    paramètre liste (list)
    paramètre valeur (type quelconque)
    Return (bool)
    """
    i = 0
    while i < len(liste):
        if liste[i] == valeur:
            return True
        i = i + 1
    return False

def recherche_indice(liste, valeur):
    """
    Description de la fonction : Renvoie l'indice de la valeur recherchée (None si valeur non présente)
    paramètre liste (list) : liste non vide
    paramètre valeur (type quelconque)
    Return (int ou Nonetype)
    """
    i = 0
    while i < len(liste):
        if liste[i] == valeur:
            return i
        i = i + 1
    return i

def recherche_minimum(liste):
    """
    Description de la fonction : Renvoie la plus petite valeur de la liste
    paramètre liste (list) : liste non vide d'entiers(int), de nombres réels(float) ou de chaîne de caractères(str)
    Return (int)
    """
    a = 500
    for e in liste:
        if e < a :
            a = e
    return a

def recherche_maximum(liste):
    """
    Description de la fonction : Renvoie la plus grande valeur de la liste
    paramètre liste (list) : liste non vide d'entiers(int), de nombres réels(float) ou de chaîne de caractères(str)
    Return (int)
    """
    a = 0
    for e in liste:
        if e > a :
            a = e
    return a

def moyenne(liste):
    """
    Description de la fonction : Calcule la moyenne des valeurs contenues dans la liste
    paramètre liste (list) : liste non vide d'entiers(int) ou de nombres réels(float)
    Return (int)
    """
    total = 0
    for e in liste :
        total = total + e
    resultat = total % len(liste)
    return resultat

moyenne(liste)