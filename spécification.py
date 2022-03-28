#exercice1
def indicemax_tableau(t):
    """
    Description de la fonction : cette fonction doit servir a donner le chifre le plus grand
    t (liste) : t dois avoir une liste remplie
    return (type) : return m
    precondition : liste remplie
    """
    assert t != [], "la liste dois être completer"
    m = 0
    for i in range(len(t)):
        if t[i] > t[m] :
            m = i
    return m

#exercice2
def divisionEuclidienne(a, b):
    """
    Description de la fonction : calcule la division entière de 2 nombres
    a, b (int) : 2 entiers
    return (tuple) : (quotient, reste)
    """
    resultat = (a//b, a%b)
    assert resultat[0]*b+resultat[1] == a , "il faut que sa soit un nombre pair" # postcondition
    return resultat

divisionEuclidienne(10, 2)