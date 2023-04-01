# Imports
import numpy as np

class Partie:
    """Classe permettant de gérer une patrie de puissance 4
    """

    # Attributs
    
    # Méthodes
    def __init__(self, joueurs_car = [1, 2], taille = (6, 7), taille_vainqueur = 4) -> None :
        """Création de la partie
        """
        # Création du tableau
        self.hauteur = taille[0]
        self.largeur = taille[1]
        self.tableau = np.zeros(taille)

        self.joueurs_car = joueurs_car # Valeur du jeton inscrite dans le tableau
        self.taille_vainqueur = taille_vainqueur # Nombre de jeton nécessaire pour gagner

    def __str__(self) -> str:
        """Permet d'afficher le tableau avec un print
        """
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
        """Retourne True si la game est terminée, ce qui signifie qu'une personne a gagné ou que tous les jetons ont été posés
        """
        # Cas où il y a un vainqueur
        if self.vainqueur()[0] :
            return True
        
        # Cas où toutes les cases sont remplies
        if not 0 in self.tableau :
            return True
        
        # Par défaut non fini
        return False

    def vainqueur(self) -> tuple[bool,int] :
        """Fonction permettant de savoir si la partie est gagné par l'un des deux joueurs et affiche le joueur gagnant le cas échéant
        Retourne en [0] si la partie est gagné par un joueur et en [1] la valeur du joueur
        """
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
                        return (True,base)

        # Colonnes
        for colonne in range(self.largeur) :
            for index in range(self.hauteur - self.taille_vainqueur + 1) :
                base = self.tableau[index][colonne]
                if base in self.joueurs_car :
                    win = True
                    for in_a_row in range(self.taille_vainqueur) :
                        if base != self.tableau[index + in_a_row][colonne] :
                            win = False
                            break
                    if win : 
                        return (True,base)
                   
        # Diagonnales
        for colonne in range(self.largeur) :
            for ligne in range(self.hauteur - self.taille_vainqueur + 1) :
                base = self.tableau[ligne][colonne]
                for direction in [1, -1] :
                    if base in self.joueurs_car :
                        win = True
                        for in_a_row in range(self.taille_vainqueur) :
                            if 0 <= colonne + direction*in_a_row < self.largeur and 0 <= ligne + in_a_row < self.hauteur :
                                if base != self.tableau[ligne + in_a_row][colonne + direction*in_a_row] :
                                    win = False
                                    break
                        if win :
                            return (True,base)
        
        return (False, None)