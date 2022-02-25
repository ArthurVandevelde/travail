from random import randint

def nettoyage_mot(mot):
    """
    Description de la fonction : met en forme un mot choisi par l'ordinateur
    mot (str) : mot comportant des caractères non souhaités (accents, majuscules, caractères retour à la ligne)
    return (str) :  mot "nettoyé" (tout en minuscule, en enlevant les accents et les retours à la ligne)
    """
    global MOT_MYSTERE
    fichier = open(nom_fichier,'r',encoding = 'utf8')
    for chiffre in range(randint(1,10)):
        chaine = fichier.readline()
    fichier.close()
    i = 0
    MOT_MYSTERE = ""
    MOT_A_DECOUVRIR = nettoyage_mot(chaine)
    while i < len(MOT_A_DECOUVRIR):
        MOT_MYSTERE = MOT_MYSTERE + '-'
        i = i + 1
    return MOT_A_DECOUVRIR, MOT_MYSTERE

def tirage_au_sort(nom_fichier):
    """
    Description de la fonction : tire au hasard un mot dans le fichier 
                                "nettoie ce mot"
                                fabrique un mot mystère composé d'autant de tirets (-) que de lettres à découvrir
    nom_fichier (str) : nom du fichier dans lequel le programme va choisir un mot
    return (tuple) : mot "nettoyé" (str), mot mystere(str)
    """
    fichier = open(nom_fichier,'r',encoding = 'utf8')
    for chiffre in range(randint(1,22274)):
        chaine = fichier.readline()
    fichier.close()
    return nettoyage_mot(chaine)

print(tirage_au_sort('dictionnaire.txt'))

def nettoyage_mot(mot):
    """
    Description de la fonction : met en forme un mot choisi par l'ordinateur
    mot (str) : mot comportant des caractères non souhaités (accents, majuscules, caractères retour à la ligne)
    return (str) :  mot "nettoyé" (tout en minuscule, en enlevant les accents et les retours à la ligne)
    """
    print(mot.lower())

def deja_choise(lettre):
    """
    Description de la fonction : Ajoute dans LETTRES_DEJA_CHOISIES les lettres choisies par le joueur
    et affiche un message informant le joueur dans le cas où il choisit une lettre déjà proposée précédemment
    lettre (str) : lettre proposée par le joueur
    return (bool) : True si la lettre a déjà été choisié, False sinon
    MODIFICATION EN PLACE de LETTRES_DEJA_CHOISIES
    """
    global LETTRES_DEJA_CHOISIES
    
    if lettre in LETTRES_DEJA_CHOISIES:
        print("lettre déja choisie")
        return True
    else:
        list_lettre = list(lettre)
        LETTRES_DEJA_CHOISIES = LETTRES_DEJA_CHOISIES + list_lettre
        return False
    

def jeu_fini():
    """
    Description de la fonction : Détermine si le jeu est fini
    return (bool) : True si le jeu est fini, False sinon
    """
    global SCORE
    global MOT_MYSTERE
    if SCORE == 0 or "-" not in MOT_MYSTERE:
        return True
    else:
        return False

def afficher_bilan():
    """
    Description de la fonction : Affiche les "messages bilans" en fin de partie (voir copie d'écran dans l'énoncé)
    return (None)
    """
    global SCORE
    global MOT_A_DECOUVRIR
    
    if SCORE == 0:
        print('Vous avez perdu !!')
        print('Le mot recherché était ' + MOT_A_DECOUVRIR)
        
    else:
        print('Bravo! Vous avez trouvé le mot ' + MOT_A_DECOUVRIR)
        print('Votre SCORE est de ' + str(SCORE))
        
def remplace_tiret(lettre):
    """
    Description de la fonction : Remplace le/les '-' par la lettre si
    lettre (str) : une lettre proposée par le joueur
    return (bool) : True si le joueur à trouver une nouvelle lettre, False sinon
    MODIFICATION DE MOT_MYSTERE
    """
    while
    
#deja_choise  fait
#jeu_fini        fait
#afficher_bilan  fait
#nettoyage_mot   fait
#tirage_au_sort  fait
#remplace_tiret
#jouer
