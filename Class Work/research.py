import turtle
from random import random, randint
import time

CURSOR_SIZE = 20

num=0
def increase_score():
    global num 
    num += 1

def my_circle(color):

    radius = randint(10, 50)

    circle = turtle.Turtle('circle', visible=False)
    circle.shapesize(radius / CURSOR_SIZE)
    circle.color(color)
    circle.penup()

    while True:
        nx = randint(2 * radius - width // 2, width // 2 - radius * 2)
        ny = randint(2 * radius - height // 2, height // 2 - radius * 2)

        circle.goto(nx, ny)

        for other_radius, other_circle in circles:
            if circle.distance(other_circle) < 2 * max(radius, other_radius):
                break
        else:
            break

    circle.showturtle()
    circle.onclick(lambda x,y,t=circle: (circle.hideturtle(), increase_score()))

    return radius, circle


screen = turtle.Screen()
screen.bgcolor("lightgreen")
screen.title("Speed Clicker")

width, height = screen.window_width(), screen.window_height()

circles = []

gameLength = 5
# Higher number means faster blocks
# 1-10
difficulty = 10
startTime = time.time()
while True:
    time.sleep(1/difficulty)

    rgb = (random(), random(), random())

    timeTaken = time.time() - startTime

    circles.append(my_circle(rgb))
    screen.title('SCORE: {}, TIME LEFT: {}'.format(num,int(round(gameLength - timeTaken,0))))

    if time.time() - startTime > gameLength: 
        break

screen.title('FINISHED! FINAL SCORE: {}'.format(num))

screen.mainloop()