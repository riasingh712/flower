import turtle
from random import randint
shelly = turtle.Turtle()
turtle.speed(0)

def star(size):
    
    for n in range(6):
        shelly.begin_fill()
        shelly.color(randint(0,255),randint(0,255),randint(0,255))
        for i in range(4):
            shelly.forward(size)
            shelly.left(90)
        shelly.end_fill()
        shelly.right(60)

turtle.Screen().bgcolor("orange")

shelly.right(90)
shelly.penup()
shelly.forward(150)
shelly.left(90)
shelly.forward(150)

shelly.pendown()
turtle.colormode(255)

star(100)


shelly.penup()
shelly.right(180)
shelly.forward(350)
shelly.pendown()

star(85)

shelly.penup()
shelly.right(90)
shelly.forward(375)
shelly.left(75)
shelly.forward(50)
shelly.pendown()

star(50)

shelly.penup()
shelly.right(180)
shelly.forward(200)
shelly.right(90)
shelly.forward(100)
shelly.pendown()

star(75)

shelly.penup()
shelly.left(120)
shelly.forward(300)
shelly.right(90)
shelly.forward(50)
shelly.pendown()

star(85)

shelly.penup()
shelly.left(180)
shelly.forward(200)
shelly.left(90)
shelly.forward(175)
shelly.pendown()

star(40)

shelly.penup()
shelly.left(30)
shelly.forward(350)
shelly.right(90)
shelly.forward(50)
shelly.pendown()

star(30)

shelly.hideturtle()






