#exercice2
##n=0
##while n<10:
##    print(n)
##    n=n+2
##    
#Exercice3
def decroissant_for(n):
    for i in range(n,0,-1):
        print(i, end='  ')
        
def decroissant_while(n):
    while n >0:
        print(n, end=' ')
        n=n-1
        
#Exercice4
def somme1(n1,n2):
    s=0
    for k in range(n1,n2):
        s=s+k
    return s

def somme2(n1,n2):
    s=0
    for k in range(n1+1,n2+1):
        s=s+k
    return s
        
# Exercice5

def nombre_alenvers (n):
    str(n)
    c =1000
    while 
    c = c / 10
#exercice6
L =700   
N = 0   
while L < 800:
    L = L*1.015
    N = N+1
print(N)
    
#exercice7

def est_premier(nombre):
    n = 2
    while n <= nombre-1:
        reponce = nombre % n
        n = n + 1
        if reponce == 0:
            return False
    else:
        return True
    
def k_premier(nombre):
    n = 2
    while n <= nombre-1:
        reponce = nombre % n
        print(reponce)
        n = n + 1
    
    
#exercice9
    
def Syracuse(nb):
    print(nb,end=' - ')
    nom = nb
    a = 0
    b = 0
    while nb > 1:
        if nb % 2 == 0 : #pair
            nb = nb // 2
            print(nb,end=' - ')
        else : #impair
            nb = nb * 3 + 1
            print(nb,end=' - ')
        a = a +1
        if nb > b:
            b = nb
    print()   
    print()
    print('Le temps du vol pour ',nom,' est de ',a,' et son altitude maximale est de ',b)
    
        
