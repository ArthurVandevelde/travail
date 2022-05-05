def Nb_tour(n):
    k = 0
    while k < n:
        if 2**k >= n:
            return k
        k = k + 1
        
print(Nb_tour(16))