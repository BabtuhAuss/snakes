from pygame.locals import Rect
import constants

class Corps:
    def __init__(self, x,y):
        """ ici on initialise le corps d'un serpent avec la tête, et le suivant en vide"""
        self.membre = Rect(x, y, constants.DIM_SNAKE, constants.DIM_SNAKE)
        self.suivant = None
        self.pred = None

    def getCoordinates(self):
        """return x,y positions"""
        return self.membre.left, self.membre.top
    def setMembre(self,x,y):
        self.membre.left=x
        self.membre.top=y
        
class Snake():

    def __init__(self):
        self.tete = Corps(0,0)
        self.dernier_x, self.dernier_y = self.tete.getCoordinates()

    def getHead(self):
        return self.tete.membre

    def ajouterMembre(self,x,y):
        nouvelleTete= Corps(x,y)
        nouvelleTete.suivant=self.tete
        self.tete.pred=nouvelleTete
        self.tete=nouvelleTete

        self.afficherCoordonnees()
        

    def avancer(self,v):

        x = self.tete
        copie_x, copie_y =x.getCoordinates()
        x.membre.move_ip(v)
        compteur=0
        while x.suivant:
            x = x.suivant
            compteur+=1
            x.setMembre(copie_x,copie_y)
            copie_x, copie_y = x.getCoordinates()




    def afficherCoordonnees(self):
        courant = self.tete
        compteur = 0
        copie_x, copie_y = courant.getCoordinates()
        while courant.suivant != None:
            print(compteur, " | x:", copie_x, " y:", copie_y)
            courant = courant.suivant
            compteur+=1
            