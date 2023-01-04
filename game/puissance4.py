# Imports
import numpy as np

class Partie:
    '''Classe permettant de gérer une patrie de puissance 4
    '''

    # Attributs
    
    # Méthodes
    def __init__(self) -> None :
        self.tableau = np.zeros((6, 7))

    def __str__(self) -> str:
        return str(self.tableau) + "\n  0  1  2  3  4  5  6"

if __name__ == "__main__" :
    print('lancé')
    p = Partie()
    print(p)