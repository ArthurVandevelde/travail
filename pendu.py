
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
        
    
#deja_choise  fait
#jeu_fini        fait
#afficher_bilan  fait
#nettoyage_mot
#tirage_au_sort
#remplace_tiret
#jouer