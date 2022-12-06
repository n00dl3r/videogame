import turtle
import random
import threading

import time
#setting up  turtle
wn = turtle.Screen()
t = turtle.Turtle()
wn.setup(600,600)
t.shape("circle")
t.speed(10)
####
turtle.listen(xdummy=None, ydummy=None)
score  = 0
def hide(x,y):
    t.hideturtle()
    global score
    score = score + 1
    print("Score:", score)


def exit():
    turtle.bye()
    #timer.cancel()

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

    

######
colors = ["red", "black", "green"]
def changecolor(x,y):
    thing = random.randint(0,2)
    color = colors[thing]
    print(color)
    t.color(color)


def com():
    randturtle()
    t.onclick(hide, btn=1, add=None)




diff = turtle.textinput("Difficuly", "Hard or easy: ")

if diff == "easy":
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
    print("start")
    randturtle()
    t.onclick(hide, btn=1, add=None)
    timer.cancel()
elif diff == "hard":
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
    print("start")
    randturtle()
    t.onclick(hide, btn=1, add=None)
    timer.cancel()


forwrite = str("Final score: " + str(score))
print(forwrite)
#t.write()




#######e

#####


#do tthe onclick clear add score and the e for exit adn the timer after each clic




#make it end
turtle.onkeypress(exit, "e")
#keeping it going
wn.mainloop()
turtle.mainloop()
input()