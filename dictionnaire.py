#exercice 2
vélo={'id':1210,"typ":"électrique","station":"la place d'Italie","statut":"en panne"}

vélo["statut"]='réparé'

#print(vélo)

# exercice 2bis

velo1={'id':1211,"typ":"électrique","station":"Le parc de velibs","statut":"en panne"}
velo2={'id':1212,"typ":"classique","station":"Le parc de velibs","statut":"dispo"}
velo3={'id':1213,"typ":"électrique","station":"eurotéléport","statut":"dispo"}

parc_velib=[]
parc_velib.append(velo1)
parc_velib.append(velo2)
parc_velib.append(velo3)

def recherche_velo1():
    nb_velo = 0
    for velo in parc_velib:
        if velo["statut"] == "dispo":
            nb_velo = nb_velo + 1
    return nb_velo

recherche_velo1()

def recherche_velo2():
    endroit = ()
    for velo in parc_velib:
        if velo["statut"] == "dispo":
            endroit = endroit + (velo["station"],)
    return endroit

#print(recherche_velo2())

#Exercice 3

