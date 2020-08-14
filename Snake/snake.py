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
        self.dernier_x, self.dernier_y = 0,0

    def getHead(self):
        return self.tete.membre

    def ajouterMembre(self):


        courant = self.tete
        while courant.suivant:
            courant = courant.suivant
        queue = Corps(self.dernier_x, self.dernier_y)

        courant.suivant=queue
        queue.pred = courant
        self.afficherCoordonnees()
        

    def avancer(self,v):
        courant = self.tete
        while courant.suivant:
            courant = courant.suivant

        while courant.pred:
            courant.setMembre(courant.pred.membre.left,courant.pred.membre.top)
            courant = courant.pred
        courant.membre.move_ip(v)



    def afficherCoordonnees(self):
        courant = self.tete
        compteur = 0
        suivant=True
        copie_x, copie_y = courant.getCoordinates()
        while suivant:
            print(compteur, " | x:", copie_x, " y:", copie_y)        
            copie_x, copie_y = courant.getCoordinates()
            compteur+=1
            courant = courant.suivant
            if not courant:
                suivant = False
        
    def mordu(self):
        position_corps = []
        courant = self.tete
        courant = courant.suivant
        while courant:
            position_corps.append([courant.membre.left, courant.membre.top])
            courant = courant.suivant
        
        return [self.tete.membre.left,self.tete.membre.top] in position_corps