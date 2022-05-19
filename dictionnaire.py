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

#exercice 3

positions = {}
positions[(48.853585, 2.301490)] = "Paris"
positions[(11.611358, 43.147752)] = "Djibouti"
positions[(37.023113, -8.996601)] = "Fortaleza de Sao Vicente"
positions[(7.677989,-5.025387)] = "Bouaké"

def localisation_photo(coordonnées,dictionnaire):
    for coord in dictionnaire.keys():
        if abs(coordonnées[0] -  coord[0]) <= 0.0001       and     abs(coordonnées[1] -  coord[1]) <= 0.0001 :
            return positions[coord]
    return None

localisation_photo((7.677989,-5.025387),positions)

# Exercice 4
def lecture(nom_fichier):
    """
    description : ouvre un fichier texte et renvoie son contenu sous la forme d'une chaîne de caractère
    paramètre nom_fichier(str) : nom du fichier
    return (str) : contenu du fichier
    """
    with open(nom_fichier,'r') as fichier:
        return fichier.read()

def occurence (chaine):
    occurence = { }
    chiffre = 0
    for lettre in chaine:
        if lettre in occurence.keys():
            occurence[lettre] =  occurence[lettre] +1
        else :
            occurence[lettre] = 1
    return occurence

print(occurence(lecture('big_brother.txt')))
