#Exercice2
def puissance(x, n):
    """
    >>> puissance(5,0)
    1
    >>> puissance(5,1)
    5
    >>> puissance(8,5)
    32768
    >>> puissance(0,5)
    0
    """
    r = 1
    for i in range(n):
        r = r * x
    return r

### exercice 3
##def appartient(v,t):
##    """
##    >>> appartient(0,0)
##    True
##    >>> appatient(6.5)
##    False
##    """
##    for element in t :
##        if v == element :
##            trouvee = True
##        else :
##            trouvee = False
##    return trouvee   
##   
##
### exercice 4
##
#Version 1

def est_croissant(t):
    """
    >>> est_croissant(0,8,9)
    True
    >>> est_croissant(3,2,1)
    False
    """
    i = len(t) - 1
    while i >= 0:
        if t[i] <= t[i+1] :
            return True
        else :
            return False
        i = i - 1
        
#Version 2

def est_croissant(t):
    """
    >>> est_croissant(0,8,9)
    True
    >>> est_croissant(3,2,1)
    False
    """
    i = len(t) - 1
    while i >= 0:
        if t[i-1] <= t[i] :
            return True
        else :
            return False
        i = i - 1
        
#Version 3

def est_croissant(t):
    """
    >>> est_croissant(0,8,9)
    True
    >>> est_croissant(3,2,1)
    False
    """
    i = len(t) - 1
    while i >= 0:
        if t[i-1] > t[i] :
            return False
        i = i - 1
    return True

#Version 4

def est_croissant(t):
    """
    >>> est_croissant(0,8,9)
    True
    >>> est_croissant(3,2,1)
    False
    """
    i = len(t) - 1
    while i > 0:
        if t[i-1] > t[i] :
            return False
        i = i - 1
    return True


if __name__ == '__main__':
    # Validation des tests
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)

