#EXERCICE A

#J'ai voulu ajouter des scores aléatoires pour les joueurs mais n'ai pas réussi à les ajouter après un "+"
import random

#Création d'un tableau pour les 5 chansons.
chansons = [1,2,3,4,5]


#Création de la classe Player qui attribuera à un joueur un pseudo et un score d'au moins 50 points pour tous les joueurs.
class Player:
    def __init__(self, pseudo, score=50):
        self.pseudo = pseudo
        self.score = score

    #Fonction qui permet d'ajouter des points au points initials du joueur.
    def chanson1(self):
        self.score += 10

    def chanson2(self):
        self.score += 20

    def chanson3(self):
        self.score += 15

    def chanson4(self):
        self.score += 23

    def chanson5(self):
        self.score += 40

    #Fonction qui permet d'afficher les points des joueurs.
    def showPoints(self):
        print("Pour cette première chanson,", self.pseudo, "a obtenu", self.score, "points.")

   
#Lignes pour définir et attribuer des caractéristiques aux joueurs.
joueur1 = Player("Joueur 1")
joueur2 = Player("Joueur 2")
joueur3 = Player("Joueur 3")

#Lignes pour appliquer les fonctions aux différents joueurs. 
joueur1.chanson1()
joueur1.showPoints()

joueur2.chanson1()
joueur2.showPoints()

joueur3.chanson1()
joueur3.showPoints()

#EXERCICE B

class Karaoke:
    def __init__(self, chansons, joueurs, ):
        return 