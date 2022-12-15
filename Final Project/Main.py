#Sources
#https://pygame.readthedocs.io/en/latest/4_text/text.html
#https://stackoverflow.com/questions/57623067/how-can-i-get-reaction-time-in-python (reaction time base)
#https://www.geeksforgeeks.org/python-display-text-to-pygame-window/ (printing on screen)
#https://www.digitalocean.com/community/tutorials/average-of-list-in-python (finding avg of reaction)
#https://bcp.instructure.com/courses/10268 and https://bcpsj-my.sharepoint.com/personal/ccozort_bcp_org/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fccozort%5Fbcp%5Forg%2FDocuments%2FDocuments%2F02%5FCourses%2FCS%2FIntro%20to%20Programming%2F2022%5FFall%2FCode&ga=1 for class notes
#https://pygame.readthedocs.io/en/latest/1_intro/intro.html

#Reaction time Game Main is my reaction time game reformated to fit the final projects standards and has a working highscore function.


#Import Librarys 
import pygame as pg
import random
from settings import *
from os import path

#universal variables
count = 0
running = True

#Game class 
class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        #Takes settings and imports them to the code with then 
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        #Sets core of game by initalizing the clock
        self.clock = pg.time.Clock()
        self.running = running = True
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data()
        
        #Creates all the text used in the file
    def draw_text(self, text, size, color, x, y):
            font = pg.font.Font(self.font_name, size)
            text_surface = font.render(text, True, color)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x, y)
            self.screen.blit(text_surface, text_rect)

    #Fetches high score data 
    def load_data(self):
        # load high score
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, HS_FILE), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0

    def run(self):
        # Game Loop
        #real time is the game time so that we can diffrenciate the play time from avg reaction time
        realtime = pg.time.get_ticks()
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            while running:
            #this closes the window when player closes it or alt+F4
                for event in pg.event.get():
                    pg.init()
        if event.type == pg.QUIT:
            running = False
            pg.quit()

        #this is where it will start the timer and start a wait timer that is within the random of 1000, 4000 
        # from the source of digital ocean
        if event.type == pg.KEYDOWN:
         if game_state == "start":
                game_state = "wait" 
                game_time = realtime + random.randint(1000, 4000)
        #game starts and starts using equation to find the avg of first time used, all times used and prints it on the screen almost on top of eachother
        # from source of class notes and comments  
        if game_state == "wait_for_reaction": 
                game_state = "wait" 
                reaction_time = (realtime - game_time) / 1000
                game_time = realtime + random.randint(1000, 4000)
                count += 1
        if game_state == "wait":
            if realtime >= game_time:
                game_state = "wait_for_reaction"   
        # this is where the magic happens with the display and posting results
        # from source of digital ocean
                averagereacttime = (averagereacttime * (count-1) + reaction_time) / count
    # reaction = FONT_NAME(f"REACTION TIME: {reaction_time:.03f}",0,(255,255,255))
    # avg_reaction = FONT_NAME(f"AVERAGE REACTION TIME IS: {averagereacttime:.03f}",0,(255,255,255))
        # telling the computer to wait if the real time is greater than the game time then if it is, it waits for player response
         
 

    def show_start_screen(self):
        # game splash/start screen
        reaction = FONT_NAME(f"REACTION TIME: {reaction_time:.03f}",0,(255,255,255))
        avg_reaction = FONT_NAME(f"AVERAGE REACTION TIME IS: {averagereacttime:.03f}",0,(255,255,255))
        self.screen.fill(BGCOLOR)
        self.draw_text(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Press a key to play", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        self.draw_text("Your Average Reaction: " + str(avg_reaction), 22, WHITE, WIDTH / 2, 15)
        pg.display.flip()
        self.wait_for_key()


    # def score(self):

    def show_go_screen(self):
        # game over/continue
        if not self.running:
            return
        self.screen.fill(BLACK)
        self.draw_text("GAME OVER", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Score: " + str(self.score), 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press a key to play again", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("FASTEST SCORE!", 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)
            with open(path.join(self.dir, HS_FILE), 'w') as f:
                f.write(str(self.score))
        else:
            self.draw_text("High Score: " + str(self.highscore), 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)
        pg.display.flip()
        
pg.quit()
