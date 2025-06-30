import pygame
from PIL import Image
from Connect4_into_class import *

class Connect4():
    def __init__(self):
        self.instance_of_Connectfour = Connectfour()
        self.screen = pygame.display.set_mode((1060, 600))
        self.board = pygame.image.load('mini-capstone/board.png').convert()
        self.board = pygame.transform.scale(self.board, (860,450))


        
    def playerBlue(self):
        self.colorBlue = (0,0,255)
        # self.player1 = pygame.draw.circle(self.screen, self.colorBlue, (232, 178), 37) 
        print("Player Blue Turn")
        self.userinput = int(input("What row are you choosing from? 1 - 7: "))
        self.worked = self.instance_of_Connectfour.userChoice(self.userinput, self.instance_of_Connectfour.place_oneBlue)
        if self.worked == True:
            self.CurPlayer = 0
            self.player1 = pygame.draw.circle(self.screen, self.colorBlue, (500, 178), 37) 
        else:
            self.CurPlayer = 1
        return self.CurPlayer
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
            self.instance_of_Connectfour.checkwinHorizonal()
            self.instance_of_Connectfour.checkwinVertical(self.instance_of_Connectfour.grid)
            self.instance_of_Connectfour.check_diagonalsBlue(self.instance_of_Connectfour.grid)
            self.instance_of_Connectfour.check_diagonalsRed(self.instance_of_Connectfour.grid)
            # self.instance_of_Connectfour.runGames()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            pygame.display.update()
        pygame.quit()



localConnect = Connect4()

localConnect.runGame()
# Connect4_into_class.runGame()
