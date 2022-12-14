
#So far this spawns a grid, places circles randomly and when clicked they add score and dissapear.
#planning on adding fps counter, reaction time top left, score top middle, and a difficulty slider. 


import turtle
import random
import threading
import time

start = time.time()

#starts the turtle library and draws the screen and the dots that you click. 
wn = turtle.Screen()
t = turtle.Turtle()
wn.setup(600,600)
t.shape("circle")
t.speed(10)

#creates the targets by its x, y plane by its "dummy"'s
turtle.listen(xdummy=None, ydummy=None)
score  = 0
def hide(x,y):
    t.hideturtle()
    global score
    score = score + 1
    print("Score:", score)

#when exited from the playing screen it kills the terminal 
def exit():
    turtle.bye()
    #timer.cancel()

#the code that randomly sends the target in the playing feild, it also has it also selects a random point of the playing feild between -290, 290 pixels.
def randturtle():
    t.color("black")
    t.penup()
    r = round(random.uniform(.5,2.25))
    t.shapesize(r)
    xc = random.randint(-290,290)
    yc = random.randint(-290,290)
    #print(xc,yc,r)
    t.hideturtle()
    t.goto(xc,yc)
    t.showturtle()

    

#computer chooses between red black and green on a 0, 1, 2 basis. then it spits out the color that it chose in its "print" function
colors = ["red", "black", "green"]
def changecolor(x,y):
    rgb = random.randint(0,2)
    color = colors[rgb]
    print(color)
    t.color(color)

#this function deals with the hit registration
def com():
    randturtle()
    t.onclick(hide, btn=1, add=None)



#Difficulty Pop Up
diff = turtle.textinput("Difficuly", "Hard or Easy: ")
#Inital timing of the game where 
if diff == "Easy":
    time.sleep(2)
    timer10 = threading.Timer(15, com)
    timer9 = threading.Timer(13.5, com)
    timer8 = threading.Timer(12, com)
    timer7 = threading.Timer(10.5, com)
    timer6 = threading.Timer(9, com)
    timer5 = threading.Timer(7.5, com)
    timer4 = threading.Timer(6, com)
    timer3 = threading.Timer(4.5, com)
    timer2 = threading.Timer(3, com)
    timer = threading.Timer(1.5, com)
    timer.start()
    timer2.start()
    timer3.start()
    timer4.start()
    timer5.start()
    timer6.start()
    timer7.start()
    timer8.start()
    timer9.start()
    timer10.start()
    print("Start")
    randturtle()
    t.onclick(hide, btn=1, add=None)
    timer.cancel()

#Hard mode with faster timers than Easy Mode
elif diff == "Hard":
    time.sleep(2)
    timer10 = threading.Timer(10, com)
    timer9 = threading.Timer(9, com)
    timer8 = threading.Timer(8, com)
    timer7 = threading.Timer(7, com)
    timer6 = threading.Timer(6, com)
    timer5 = threading.Timer(5, com)
    timer4 = threading.Timer(4, com)
    timer3 = threading.Timer(3, com)
    timer2 = threading.Timer(2, com)
    timer = threading.Timer(1, com)
    timer.start()
    timer2.start()
    timer3.start()
    timer4.start()
    timer5.start()
    timer6.start()
    timer7.start()
    timer8.start()
    timer9.start()
    timer10.start()
    print("Start")
    randturtle()
    t.onclick(hide, btn=1, add=None)
    timer.cancel()

timer_text = turtle.Turtle()


#once closed print final clicks on black dots in terminal
finalScore = str("Final score: " + str(score))
print(finalScore)

#make it end with the e key
turtle.onkeypress(exit, "e")
wn.mainloop()
turtle.mainloop()
input()