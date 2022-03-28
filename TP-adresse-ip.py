def sous_reseau (ip,masque):
    a = ip.split(".")
    b=masque.split(".")
    for i in range(4):
        c= str(a[i]) & str(b[i])
    return c

sous_reseau(192.168.16.8,255.255.0.0)