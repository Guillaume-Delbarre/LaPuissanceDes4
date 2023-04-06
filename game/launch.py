from puissance4 import Partie
from humain import Humain

"""
Script principal permettant de créer une partie de puissance4 en choigissant le type des joueurs
"""

# Création de tous les types de joueurs possibles
type_joueurs = {
    "H" : {
        "nom" : "Humain",
        "class" : Humain
    }
}

# Liste des codes possibles avec tous les joueurs possibles
list_code = list(type_joueurs.keys())

if __name__ == "__main__" :
    # Introduction et choix des joueurs
    print("Bienvenue dans le jeu de puissance4")
    joueurs = [None, None]
    print(list_code)
    code1 = ""
    while code1 not in list_code :
        print(f"Veuillez choisir le joueur numéro 1 : {list_code}")
        code1 = input("H -> Humain :\n")
    joueurs[0] = type_joueurs[code1]["class"]()

    code2 = ""
    while code2 not in list_code :
        print(f"Veuillez choisir le joueur numéro 2 : {list_code}")
        code2 = input("H -> Humain :\n")
    joueurs[1] = type_joueurs[code2]["class"]()

    p = Partie()
    while not p.is_finished() :
        joueurs[p.to_play].placer_jeton(partie=p, id_joueur=p.to_play)
    
    vainqueur = p.vainqueur()

    print(p)
    if vainqueur[0] :
        print(f"Le joueur numéro {vainqueur[1] + 1} a gagné")
    else :
        print("Match nul")