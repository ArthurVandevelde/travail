def sous_reseau (ip,masque):
    c = []
    a = ip.split(".")
    b=masque.split(".")
    for i in range(4):
        c= c + a[i] & b[i]
    return c

sous_reseau(192.168.16.8,255.255.0.0)
