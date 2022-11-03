# i want to make a game that tracks reacion time by having the backround turn either red or green and making player click 3 dots randomly while timed
# there should be a timer when the screen turns from red to green
# when screen turnes green start timer and set 3 random black dots on the screen


# new comment 
#Sources
#https://pygame.readthedocs.io/en/latest/4_text/text.html
#https://stackoverflow.com/questions/57623067/how-can-i-get-reaction-time-in-python (reaction time base)
#https://www.geeksforgeeks.org/python-display-text-to-pygame-window/ (printing on screen)
#https://www.digitalocean.com/community/tutorials/average-of-list-in-python (finding avg of reaction)
#https://bcp.instructure.com/courses/10268 and https://bcpsj-my.sharepoint.com/personal/ccozort_bcp_org/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fccozort%5Fbcp%5Forg%2FDocuments%2FDocuments%2F02%5FCourses%2FCS%2FIntro%20to%20Programming%2F2022%5FFall%2FCode&ga=1 for class notes
#https://pygame.readthedocs.io/en/latest/1_intro/intro.html

import pygame
import random
pygame.init()

#sets the game into a screen popup and displays the name of the game
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Reaction Time game")

#found a font that is pleasing to the eye
font = pygame.font.SysFont('arial', 30)

#displays a way to start the game in the center of the screen
text = font.render("PRESS ANY KEY TO START ", 0, (255,255,255))
# font = font.render("PRESS ANY KEY",0,(0,255,0))

#Universal claims
reaction = None
avg_reaction = None
highscore = None

#preemptively starting the loop and giving vairables 
game_state = "start"
game_time = 0
averagereacttime = 0
count = 0

#started loop and created a ticker to create ingame time
running = True
while running:
    #real time is the game time so that we can diffrenciate the play time from avg reaction time
    realtime = pygame.time.get_ticks()
    #this closes the window when player closes it or alt+F4
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    #this is where it will start the timer and start a wait timer that is within the random of 1000, 4000 
    # from the source of digital ocean
        if event.type == pygame.KEYDOWN:
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
    # this is where the magic happens with the display and posting results
    # from source of digital ocean
                averagereacttime = (averagereacttime * (count-1) + reaction_time) / count
                reaction = font.render(f"REACTION TIME: {reaction_time:.03f}",0,(255,255,255))
                avg_reaction = font.render(f"AVERAGE REACTION TIME IS: {averagereacttime:.03f}",0,(255,255,255))
# telling the computer to wait if the real time is greater than the game time then if it is, it waits for player response
    if game_state == "wait":
        if realtime >= game_time:
            game_state = "wait_for_reaction"        

# refreshes the page basicaly and make teh entire window black again
    screen.fill(pygame.Color("Black"))
    
    #gets the center of the screen to "start":
    center = screen.get_rect().center
    if game_state == "start":
        screen.blit(text, text.get_rect(center = center))
    # waits for the next input of player
    if game_state == "wait_for_reaction":
        screen.blit(text, text.get_rect(center = center))
    # reaction of most previous attempt "score"
    if reaction:
        screen.blit(reaction, reaction.get_rect(center = (center[0], 350)))
    # average reaction of all attempts 
    if avg_reaction:
        screen.blit(avg_reaction, avg_reaction.get_rect(center = (center[0], 400)))

# im using flip instead of update because im not having any bots or sprites on my screen and flip just updates the entire screen where as updateing an individual sprite updates per entity
    pygame.display.flip()

# i tried to make a backround be an image of a monkey but i toataly forgot how to import my file as a path. 