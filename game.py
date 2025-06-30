import pygame
import sys
from button import Button
import tkinter
from Connect4_into_class import *



class Main:


    def get_font(self, size): 
        return pygame.font.Font("connect-game/assets/fonts/LemonMilk.ttf", size)



    def __init__(self):
        pygame.init()
        root = tkinter.Tk()
        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()
        self.native_res = (self.width, self.height)
        root.destroy()
        self.screen = pygame.display.set_mode((1280,720), pygame.RESIZABLE) 
        self.w = self.screen.get_width()
        self.h = self.screen.get_height()
        self.display = pygame.Surface((350, 200))
        self.clock = pygame.time.Clock()


    
    def run(self):
        play_instance = screen_play.play_screen
        options_instance = screen_options.options_screen
        # self.clock.tick(60)
        screen_mainmenu.main_menu(play_instance, options_instance)


class screen_mainmenu:
        def main_menu(self, play_inst):
            main_instance = Main()
            play_inst = screen_play()
            options_inst = screen_options()
            
            pygame.display.set_caption("Main Menu")
            while True:
                self.image = pygame.image.load("connect-game/assets/BG.jpg")
                # self.imageBoard = pygame.image.load('mini-capstone/board.png')
                self.scaled_image = pygame.transform.scale(self.image, (main_instance.w, main_instance.h))
                main_instance.screen.blit(self.scaled_image, (0,0))

                menu_mouse_pos = pygame.mouse.get_pos()


                MENU_TEXT = main_instance.get_font(100).render("CONNECT 4", True, "#fdfdfd")
                MENU_RECT = MENU_TEXT.get_rect(center=(main_instance.w//2, (main_instance.h//2)-(main_instance.h//9)*3.8))

                play_button = Button(image=pygame.image.load("connect-game/assets/RECT pngs/Play Rect.png"), pos=(main_instance.w//2, (main_instance.h//2) - ((main_instance.h//8.6)*2)), 
                                    text_input="PLAY", font=main_instance.get_font(90), base_color="#1d72bc", hovering_color="White")
                options_button = Button(image=pygame.image.load("connect-game/assets/RECT pngs/Options Rect.png"), pos=(main_instance.w//2, (main_instance.h//2)), 
                                    text_input="OPTIONS", font=main_instance.get_font(90), base_color="#1d72bc", hovering_color="White")
                quit_button = Button(image=pygame.image.load("connect-game/assets/RECT pngs/Quit Rect.png"), pos=(main_instance.w//2, (main_instance.h//2) + ((main_instance.h//8.6)*2)), 
                                    text_input="QUIT", font=main_instance.get_font(90), base_color="#1d72bc", hovering_color="White")

                main_instance.screen.blit(MENU_TEXT, MENU_RECT)

                for button in [play_button, options_button, quit_button]:
                    button.changeColor(menu_mouse_pos)
                    button.update(main_instance.screen)
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                        
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if play_button.checkForInput(menu_mouse_pos):
                            if event.button == 1:
                                play_inst.play_screen()
                        if options_button.checkForInput(menu_mouse_pos):
                            if event.button == 1:
                                options_inst.options_screen()
                        if quit_button.checkForInput(menu_mouse_pos):
                            if event.button == 1:
                                pygame.quit()
                                sys.exit()


                
                pygame.display.update()


class screen_play:
        def play_screen(self):
            main_instance = Main()
            play_instance = screen_play.play_screen
            options_instance = screen_options.options_screen
            gameCSV_instance = Connectfour()
            pygame.display.set_caption("Play")
            self.CurPlayer = 1
            while True:
                main_instance.screen.fill('black')
                self.play_mouse_pos = pygame.mouse.get_pos()
                

                # self.back_button = Button(image=pygame.image.load("connect-game/assets/RECT pngs/Back Rect.png"), pos=(main_instance.w//2, (main_instance.h//2) + ((main_instance.h//9)*2)), 
                #                     text_input="Back", font=main_instance.get_font(90), base_color="#1d72bc", hovering_color="White")
                self.image1 = pygame.image.load("connect-game/assets/RECT pngs/Back Rect.png")
                self.back_buttonTransform = pygame.transform.scale(self.image1, (200, 60))                         
                self.back_button = Button(image= self.back_buttonTransform, pos = (70,20), 
                                    text_input="Back", font=main_instance.get_font(20), base_color="#1d72bc", hovering_color="White")
                self.back_button.changeColor(self.play_mouse_pos)
                self.back_button.update(main_instance.screen)
                

                #Column1
                self.Column1 = pygame.image.load("connect-game/assets/RECT pngs/Back Rect.png")
                self.Column1Trans = pygame.transform.scale(self.Column1, (150, 60))                         
                self.Column1Button = Button(image= self.Column1Trans, pos = (345,60), 
                                    text_input="Column 1", font=main_instance.get_font(20), base_color="#1d72bc", hovering_color="White")
                self.Column1Button.changeColor(self.play_mouse_pos)
                self.Column1Button.update(main_instance.screen)

                
                # #Column2
                self.Column2 = pygame.image.load("connect-game/assets/RECT pngs/Back Rect.png")
                self.Column2Trans = pygame.transform.scale(self.Column2, (150, 60))                         
                self.Column2Button = Button(image= self.Column2Trans, pos = (555,60), 
                                    text_input="Column 2", font=main_instance.get_font(20), base_color="#1d72bc", hovering_color="White")
                self.Column2Button.changeColor(self.play_mouse_pos)
                self.Column2Button.update(main_instance.screen)
                
                # #Column3
                self.Column3 = pygame.image.load("connect-game/assets/RECT pngs/Back Rect.png")
                self.Column3Trans = pygame.transform.scale(self.Column3, (150, 60))                         
                self.Column3Button = Button(image= self.Column3Trans, pos = (760,60), 
                                    text_input="Column 3", font=main_instance.get_font(20), base_color="#1d72bc", hovering_color="White")
                self.Column3Button.changeColor(self.play_mouse_pos)
                self.Column3Button.update(main_instance.screen)
                
                # #Column4
                self.Column4 = pygame.image.load("connect-game/assets/RECT pngs/Back Rect.png")
                self.Column4Trans = pygame.transform.scale(self.Column4, (150, 60))                         
                self.Column4Button = Button(image= self.Column4Trans, pos = (960,60), 
                                    text_input="Column 4", font=main_instance.get_font(20), base_color="#1d72bc", hovering_color="White")
                self.Column4Button.changeColor(self.play_mouse_pos)
                self.Column4Button.update(main_instance.screen)
                
                # #Column5
                self.Column5 = pygame.image.load("connect-game/assets/RECT pngs/Back Rect.png")
                self.Column5Trans = pygame.transform.scale(self.Column5, (150, 60))                         
                self.Column5Button = Button(image= self.Column5Trans, pos = (1170,60), 
                                    text_input="Column 5", font=main_instance.get_font(20), base_color="#1d72bc", hovering_color="White")
                self.Column5Button.changeColor(self.play_mouse_pos)
                self.Column5Button.update(main_instance.screen)
                
                #Column6
                self.Column6 = pygame.image.load("connect-game/assets/RECT pngs/Back Rect.png")
                self.Column6Trans = pygame.transform.scale(self.Column6, (150, 60))                         
                self.Column6Button = Button(image= self.Column6Trans, pos = (1377,60), 
                                    text_input="Column 6", font=main_instance.get_font(20), base_color="#1d72bc", hovering_color="White")
                self.Column6Button.changeColor(self.play_mouse_pos)
                self.Column6Button.update(main_instance.screen)

                #Column 7
                self.Column7 = pygame.image.load("connect-game/assets/RECT pngs/Back Rect.png")
                self.Column7Trans = pygame.transform.scale(self.Column7, (150, 60))                         
                self.Column7Button = Button(image= self.Column7Trans, pos = (1585,60), 
                                    text_input="Column 7", font=main_instance.get_font(20), base_color="#1d72bc", hovering_color="White")
                self.Column7Button.changeColor(self.play_mouse_pos)
                self.Column7Button.update(main_instance.screen)




                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                     #--------------------------------- PLAYER BLUE BELOW------------------------------
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.CurPlayer == 1:
                                if self.Column1Button.checkForInput(self.play_mouse_pos):
                                    if event.button == 1:
                                        self.worked =  gameCSV_instance.userChoice(0,gameCSV_instance.place_oneBlue)
                                        if self.worked == True:
                                            self.CurPlayer = 0
                                        else:
                                            self.CurPlayer = 1
                                        gameCSV_instance.checkwinHorizonal()
                                        gameCSV_instance.checkwinVertical(gameCSV_instance.grid)
                                        gameCSV_instance.check_diagonalsRed(gameCSV_instance.grid)
                                elif self.Column2Button.checkForInput(self.play_mouse_pos):
                                    if event.button == 1:
                                        self.worked = gameCSV_instance.userChoice(1,gameCSV_instance.place_oneBlue)
                                        if self.worked == True:
                                            self.CurPlayer = 0
                                        else:
                                            self.CurPlayer = 1
                                        gameCSV_instance.checkwinHorizonal()
                                        gameCSV_instance.checkwinVertical(gameCSV_instance.grid)
                                        gameCSV_instance.check_diagonalsRed(gameCSV_instance.grid)
                                elif self.Column3Button.checkForInput(self.play_mouse_pos):
                                    if event.button == 1:
                                       self.worked =  gameCSV_instance.userChoice(2,gameCSV_instance.place_oneBlue)
                                       if self.worked == True:
                                         self.CurPlayer = 0
                                       else:
                                            self.CurPlayer = 1
                                       gameCSV_instance.checkwinHorizonal()
                                       gameCSV_instance.checkwinVertical(gameCSV_instance.grid)
                                       gameCSV_instance.check_diagonalsRed(gameCSV_instance.grid)
                                elif self.Column4Button.checkForInput(self.play_mouse_pos):
                                    if event.button == 1:
                                       self.worked =  gameCSV_instance.userChoice(3,gameCSV_instance.place_oneBlue)
                                       if self.worked == True:
                                            self.CurPlayer = 0
                                       else:
                                            self.CurPlayer = 1
                                       gameCSV_instance.checkwinHorizonal()
                                       gameCSV_instance.checkwinVertical(gameCSV_instance.grid)
                                       gameCSV_instance.check_diagonalsRed(gameCSV_instance.grid)
                                elif self.Column5Button.checkForInput(self.play_mouse_pos):
                                    if event.button == 1:
                                        self.worked = gameCSV_instance.userChoice(4,gameCSV_instance.place_oneBlue)
                                        if self.worked == True:
                                            self.CurPlayer = 0
                                        else:
                                            self.CurPlayer = 1
                                        gameCSV_instance.checkwinHorizonal()
                                        gameCSV_instance.checkwinVertical(gameCSV_instance.grid)
                                        gameCSV_instance.check_diagonalsRed(gameCSV_instance.grid)
                                elif self.Column6Button.checkForInput(self.play_mouse_pos):
                                    if event.button == 1:
                                       self.worked =  gameCSV_instance.userChoice(5,gameCSV_instance.place_oneBlue)
                                       if self.worked == True:
                                            self.CurPlayer = 0
                                       else:
                                            self.CurPlayer = 1
                                       gameCSV_instance.checkwinHorizonal()
                                       gameCSV_instance.checkwinVertical(gameCSV_instance.grid)
                                       gameCSV_instance.check_diagonalsRed(gameCSV_instance.grid)
                                elif self.Column7Button.checkForInput(self.play_mouse_pos):
                                    if event.button == 1:
                                        self.worked = gameCSV_instance.userChoice(6,gameCSV_instance.place_oneBlue)
                                        if self.worked == True:
                                            self.CurPlayer = 0
                                        else:
                                            self.CurPlayer = 1
                                        gameCSV_instance.checkwinHorizonal()
                                        gameCSV_instance.checkwinVertical(gameCSV_instance.grid)
                                        gameCSV_instance.check_diagonalsRed(gameCSV_instance.grid)

                                        #--------------------------------- PLAYER RED BELOW------------------------------

                        elif self.CurPlayer == 0:
                            if self.Column1Button.checkForInput(self.play_mouse_pos):
                                if event.button == 1:
                                    self.worked =  gameCSV_instance.userChoice(0,gameCSV_instance.place_oneRed)
                                    if self.worked == True:
                                        self.CurPlayer = 1
                                    else:
                                        self.CurPlayer = 0
                                    gameCSV_instance.checkwinHorizonal()
                                    gameCSV_instance.checkwinVertical(gameCSV_instance.grid)
                                    gameCSV_instance.check_diagonalsRed(gameCSV_instance.grid)
                            elif self.Column2Button.checkForInput(self.play_mouse_pos):
                                if event.button == 1:
                                    self.worked = gameCSV_instance.userChoice(1,gameCSV_instance.place_oneRed)
                                    if self.worked == True:
                                        self.CurPlayer = 1
                                    else:
                                        self.CurPlayer = 0
                                    gameCSV_instance.checkwinHorizonal()
                                    gameCSV_instance.checkwinVertical(gameCSV_instance.grid)
                                    gameCSV_instance.check_diagonalsRed(gameCSV_instance.grid)
                            elif self.Column3Button.checkForInput(self.play_mouse_pos):
                                if event.button == 1:
                                    self.worked =  gameCSV_instance.userChoice(2,gameCSV_instance.place_oneRed)
                                    if self.worked == True:
                                        self.CurPlayer = 1
                                    else:
                                        self.CurPlayer = 0
                                    gameCSV_instance.checkwinHorizonal()
                                    gameCSV_instance.checkwinVertical(gameCSV_instance.grid)
                                    gameCSV_instance.check_diagonalsRed(gameCSV_instance.grid)
                            elif self.Column4Button.checkForInput(self.play_mouse_pos):
                                if event.button == 1:
                                    self.worked =  gameCSV_instance.userChoice(3,gameCSV_instance.place_oneRed)
                                    if self.worked == True:
                                        self.CurPlayer = 1
                                    else:
                                        self.CurPlayer = 0
                                    gameCSV_instance.checkwinHorizonal()
                                    gameCSV_instance.checkwinVertical(gameCSV_instance.grid)
                                    gameCSV_instance.check_diagonalsRed(gameCSV_instance.grid)
                            elif self.Column5Button.checkForInput(self.play_mouse_pos):
                                if event.button == 1:
                                    self.worked = gameCSV_instance.userChoice(4,gameCSV_instance.place_oneRed)
                                    if self.worked == True:
                                        self.CurPlayer = 1
                                    else:
                                        self.CurPlayer = 0
                                    gameCSV_instance.checkwinHorizonal()
                                    gameCSV_instance.checkwinVertical(gameCSV_instance.grid)
                                    gameCSV_instance.check_diagonalsRed(gameCSV_instance.grid)
                            elif self.Column6Button.checkForInput(self.play_mouse_pos):
                                if event.button == 1:
                                    self.worked =  gameCSV_instance.userChoice(5,gameCSV_instance.place_oneRed)
                                    if self.worked == True:
                                        self.CurPlayer = 1
                                    else:
                                        self.CurPlayer = 0
                                    gameCSV_instance.checkwinHorizonal()
                                    gameCSV_instance.checkwinVertical(gameCSV_instance.grid)
                                    gameCSV_instance.check_diagonalsRed(gameCSV_instance.grid)
                            elif self.Column7Button.checkForInput(self.play_mouse_pos):
                                if event.button == 1:
                                    self.worked = gameCSV_instance.userChoice(6,gameCSV_instance.place_oneRed)
                                    if self.worked == True:
                                        self.CurPlayer = 1
                                    else:
                                        self.CurPlayer = 0
                                    gameCSV_instance.checkwinHorizonal()
                                    gameCSV_instance.checkwinVertical(gameCSV_instance.grid)
                                    gameCSV_instance.check_diagonalsRed(gameCSV_instance.grid)
                        

                        

                
                # self.play_text = main_instance.get_font(45).render("This is the PLAY screen.", True, "White")
                # self.play_rect = self.play_text.get_rect(center=(main_instance.w//2, (main_instance.h//2)))
                # main_instance.screen.blit(self.play_text, self.play_rect)
                self.imageBoard = pygame.image.load('mini-capstone/board.png')
                self.scaled_image2 = pygame.transform.scale(self.imageBoard, (1520, 870))
                main_instance.screen.blit(self.scaled_image2, (200,100))

            
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.QUIT, sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.back_button.checkForInput(self.play_mouse_pos):
                            if event.button == 1:
                                screen_mainmenu.main_menu(play_instance, options_instance)

                pygame.display.update()
                pygame.display.flip()


class screen_options:
    def options_screen(self):
        main_instance = Main()
        play_instance = screen_play.play_screen
        options_instance = screen_options.options_screen
        pygame.display.set_caption("Options")
        while True:
            main_instance.screen.fill('black')
            self.options_mouse_pos = pygame.mouse.get_pos()


            self.back_button = Button(image=pygame.image.load("connect-game/assets/RECT pngs/Back Rect.png"), pos=(main_instance.w//2, (main_instance.h//2) + ((main_instance.h//9)*2)), 
                            text_input="Back", font=main_instance.get_font(75), base_color="#1d72bc", hovering_color="White") 
            self.back_button.changeColor(self.options_mouse_pos)
            self.back_button.update(main_instance.screen)
            
            self.options_text = main_instance.get_font(45).render("This is the OPTIONS screen.", True, "White")
            self.options_rect = self.options_text.get_rect(center=(main_instance.w//2, (main_instance.h//2)))
            main_instance.screen.blit(self.options_text, self.options_rect)


            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.QUIT, sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.back_button.checkForInput(self.options_mouse_pos):
                            if event.button == 1:
                                screen_mainmenu.main_menu(play_instance, options_instance)

            pygame.display.update()
            pygame.display.flip()


run_instance = Main()
run_instance.run()

#play:Callable, options:Callable, exit:Callable