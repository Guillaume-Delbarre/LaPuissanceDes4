from puissance4 import Partie

# Interface utilisée par tous les types de joueurs
class JoueurInterface :
    
    def placer_jeton(self, partie: Partie, id_joueur: int):
        """Place un jeton dans le tableau avec ajout_jeton"""
        pass