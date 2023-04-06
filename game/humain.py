from joueur_interface import JoueurInterface
from puissance4 import Partie

class Humain(JoueurInterface):

    def __init__(self) -> None:
        pass

    def placer_jeton(self, partie: Partie, id_joueur: int):
        print(f"Vous êtes le joueur : {partie.joueurs_car[id_joueur]}")
        place = False
        while not place :
            try :
                pos = int(input(f"Indiquez la colonne où jouer : \n {partie}\n"))
                place = partie.ajout_jeton(colonne=pos, joueur_id=id_joueur)
            except :
                print("La valeurs entrée n'est pas correcte, veuillez entrer un nombre")
            