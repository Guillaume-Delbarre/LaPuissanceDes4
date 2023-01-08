# Imports
import numpy as np

class Partie:
    """Classe permettant de gérer une patrie de puissance 4
    """

    # Attributs
    
    # Méthodes
    def __init__(self, joueurs_car = [1, 2], taille = (6, 7), taille_vainqueur = 4) -> None :
        # Création du tableau
        self.hauteur = taille[0]
        self.largeur = taille[1]
        self.tableau = np.zeros(taille)

        self.joueurs_car = joueurs_car # Valeur du jeton inscrite dans le tableau
        self.taille_vainqueur = taille_vainqueur # Nombre de jeton nécessaire pour gagner

    def __str__(self) -> str:
        return str(self.tableau) + "\n  " + "  ".join([str(i) for i in range(self.largeur)])

    def ajout_jeton(self, colonne: int, joueur_id: int) -> bool :
        """Ajoute un jeton 'joueur_id' dans la colonne 'colonne' voulue
        Retourne False si le pion n'a pas pu être placé
        """
        if colonne not in [*range(self.largeur)] :
            return False
        if joueur_id not in [0, 1] :
            return False
        for ligne in reversed(range(self.hauteur)) :
            if self.tableau[ligne][colonne] == 0 :
                self.tableau[ligne][colonne] = self.joueurs_car[joueur_id]
                return True
        return False
    
    def is_finished(self) -> bool :
        return self.vainqueur() in self.joueurs_car

    def vainqueur(self) -> int :
        # Lignes
        for ligne in self.tableau :
            for index in range(self.largeur - self.taille_vainqueur + 1) :
                base = ligne[index]
                if base in self.joueurs_car :
                    win = True
                    for in_a_row in range(self.taille_vainqueur) :
                        if base != ligne[index + in_a_row] :
                            win = False
                            break
                    if win :
                        return base

        # Colonnes
        for colonne in self.largeur :
            for index in range(self.hauteur - self.taille_vainqueur + 1) :
                base = self.tableau[index][colonne]
                if base in self.joueurs_car :
                    win = True
                    for in_a_row in range(self.taille_vainqueur) :
                        if base != self.tableau[index + in_a_row][colonne] :
                            win = False
                            break
                    if win : 
                        return base
        # Diagonnales


if __name__ == "__main__" :
    print('lancé')
    p = Partie()
    p.ajout_jeton(0, 0)
    p.ajout_jeton(5, 1)
    p.ajout_jeton(2, 1)
    # p.ajout_jeton(3, 1)
    p.ajout_jeton(4, 1)
    p.ajout_jeton(6, 1)
    print(p)
    print(p.vainqueur())