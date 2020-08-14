import pygame, sys
from pygame.locals import *
import constants
from Snake.snake import *
import random


def dessiner_snake(screen,s):
    suivant = True
    x=s.tete
    while suivant:
        pygame.draw.rect(screen, constants.BLUE, x.membre)
        x=x.suivant
        if x == None:
            suivant=False

def actualiser(screen,s,fruit):
    pygame.time.delay(100)
    screen.fill(constants.WHITE)
    dessiner_snake(screen,s)
    pygame.draw.rect(screen, constants.FRUIT, fruit)
    pygame.display.flip()

def ajouter_fruit():
    rand_x = random.randrange(0, constants.WINDOW_W-constants.DIM_SNAKE, constants.DIM_SNAKE)
    rand_y = random.randrange(0, constants.WINDOW_H-constants.DIM_SNAKE, constants.DIM_SNAKE)
    fruit = Rect(rand_x, rand_y, constants.DIM_SNAKE, constants.DIM_SNAKE)
    return fruit, rand_x, rand_y
def main():
    score = 0
    pygame.init()
    s = Snake()

    v = [0, 0]
    screen=pygame.display.set_mode((constants.WINDOW_W,constants.WINDOW_H))
    fruit, fruit_x,fruit_y = ajouter_fruit()
    actualiser(screen,s,fruit)
    touchee = False
    launch=False
    while not touchee:
        for event in pygame.event.get():
            if event.type == QUIT:
                touchee = True
            if event.type == KEYDOWN:
                if event.key in constants.DIR_HEAD:
                    v = constants.DIR_HEAD[event.key]
                    launch=True
                    
                                
        if launch:
            x_tete, y_tete = s.tete.getCoordinates()
            if(x_tete==fruit_x and y_tete==fruit_y):
                s.ajouterMembre()
                score+=1
                fruit,fruit_x,fruit_y=ajouter_fruit()

            #verif bordures
            if s.getHead().left < 0 or s.getHead().right > constants.WINDOW_W-5 or s.getHead().top < 0-5 or s.getHead().bottom > constants.WINDOW_H+5 :
                touchee = True
            
            if s.mordu():
                touchee = True

            s.avancer(v)
            
            actualiser(screen,s,fruit)
        
    pygame.quit()
    print(score)



main()