import turtle
import random
colors = ["gold", "orange", "yellow"]
# ---------- Setup ----------
t = turtle.Turtle()
screen = turtle.Screen()
t.shape("turtle")
t.speed(0)
t.pensize(1)
#t.pencolor("black")
t.pencolor("azure")
t.fillcolor("orange")
screen.bgcolor("darkblue")
screen.setup(1000, 500)

def go(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_moon():
    t.setheading(0)
    t.fillcolor("azure")
    t.begin_fill()
    for i in range(18):
        t.forward(20)
        t.left(10)
    t.right(180)
    for i in range(18):
        t.forward(20)
        t.right(10)
    t.end_fill()

def five_pointed_star():
    t.begin_fill()
    size = random.randint(5, 75)
    t.fillcolor(colors[random.randint(0, 2)])
    t.left(random.randint(1, 72))
    for i in range(5):
        t.forward(size)
        t.right(144)
        t.forward(size)
        t.left(72)
    t.end_fill()

def draw_circle():
    t.setheading(0)
    t.begin_fill()
    for i in range(36):
        t.forward(4)
        t.left(10)
    t.right(180)
    t.end_fill()

def draw_cloud():
    t.fillcolor("lightsteelblue")
    t.pencolor("lightsteelblue")
    t.penup()
    x = random.randint(-500, 500)
    y = random.randint(-250, 250)
    t.goto(x, y)
    for i in range(5):
        direction = random.randint(0, 360)
        t.pendown()
        draw_circle()
        t.penup()
        t.right(direction)
        t.forward(30)


for i in range(15):
    go(random.randint(-500,500),random.randint(-250,250))
    five_pointed_star()
go(random.randint(-350,350),random.randint(0,100))
draw_moon()
for i in range(15):
    go(random.randint(-500, 500), random.randint(-250, 250))
    draw_cloud()



screen.exitonclick()
