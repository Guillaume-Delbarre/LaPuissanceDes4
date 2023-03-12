import unittest
import sys

# Add new path to import game
sys.path.append(sys.path[0][:-5])
from game.puissance4 import Partie

class TestGame(unittest.TestCase) :

    def test_create_game(self) :
        p = Partie()
        self.assertIsInstance(p, Partie)

    def test_ajout_jeton(self) :
        p = Partie(taille=(6, 7))
        self.assertTrue(p.ajout_jeton(0, 0))
        self.assertTrue(p.ajout_jeton(0, 0))
        self.assertTrue(p.ajout_jeton(0, 0))
        self.assertTrue(p.ajout_jeton(0, 0))
        self.assertTrue(p.ajout_jeton(0, 0))
        self.assertTrue(p.ajout_jeton(0, 0))
        self.assertFalse(p.ajout_jeton(0, 0))
        self.assertFalse(p.ajout_jeton(-1, 0))
        self.assertFalse(p.ajout_jeton(0, 2))
    
    def test_gagnant_ligne(self) :
        p1 = Partie(taille_vainqueur=3)
        print(p1)
        p1.ajout_jeton(colonne=0, joueur_id=0)
        p1.ajout_jeton(0, 0)
        p1.ajout_jeton(1, 0)
        p1.ajout_jeton(3, 0)
        print(p1)
        self.assertFalse(p1.vainqueur()[0])
        self.assertIsNone(p1.vainqueur()[1])
        p1.ajout_jeton(2, 0)
        print(p1)
        self.assertTrue(p1.vainqueur()[0])
        self.assertEqual(p1.vainqueur()[1], 1)

    def test_gagnant_colonne(self) :
        p1 = Partie(taille_vainqueur=5, joueurs_car = [4, 5])
        p1.ajout_jeton(colonne=0, joueur_id=1)
        p1.ajout_jeton(colonne=0, joueur_id=1)
        p1.ajout_jeton(colonne=0, joueur_id=1)
        p1.ajout_jeton(colonne=0, joueur_id=1)
        self.assertFalse(p1.vainqueur()[0])
        self.assertIsNone(p1.vainqueur()[1])
        p1.ajout_jeton(colonne=1, joueur_id=1)
        self.assertFalse(p1.vainqueur()[0])
        self.assertIsNone(p1.vainqueur()[1])
        p1.ajout_jeton(colonne=0, joueur_id=1)
        self.assertTrue(p1.vainqueur()[0])
        self.assertEqual(p1.vainqueur()[1], 5)


if __name__ == "__main__" :
    unittest.main()