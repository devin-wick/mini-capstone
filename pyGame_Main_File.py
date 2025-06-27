import pygame
from PIL import Image
#pygame.init()
import Connect4_into_class
from Connect4_into_class import *

class Connect4():
    def __init__(self):
        self.instance_of_Connectfour = Connectfour()
        self.screen = pygame.display.set_mode((1060, 600))
        self.board = pygame.image.load('board.png').convert()
        self.board = pygame.transform.scale(self.board, (860,450))
        
    def playerBlue(self):
        self.colorBlue = (0,0,255)
        self.player1 = pygame.draw.circle(self.screen, self.colorBlue, (232, 178), 37) 
    def playerRED(self):
        self.colorRed = (255,0,0)
        self.player1 = pygame.draw.circle(self.screen, self.colorRed, (338, 178), 37) 
 

    def runGame(self):
        self.yellow = (255,255,0)
        self.run = True
        while self.run == True:
   
            self.screen.fill(self.yellow)
            self.screen.blit(self.board,(100, 80))
            self.playerBlue()
            self.playerRED()
            # self.instance_of_Connectfour.runGames()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            pygame.display.update()
        pygame.quit()



localConnect = Connect4()

localConnect.runGame()
# Connect4_into_class.runGame()
