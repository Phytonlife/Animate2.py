import turtle

t = turtle.Turtle()
# чтобы рисовалось побыстрее
t.speed(0)
#рисовать квадрат
def square():

    for i in range(4):

        t.forward(100)

        t.left(90)

# движения карандаша
def move(x, y):
    t.up()
    t.goto(x, y)
    t.down()


def circle():
    for i in range(60):
        t.forward(5)
        t.left(6)

# spiral()
def spiral():
    for i in range(160):
        t.forward(i / 10)
        t.left(15)


# star()

def star():
    for i in range(5):
        t.forward(100)
        t.right(144)

#скорость и холст карандаша
# t.speed(10)
# t.shape("turtle")

# olympic_logo()
# for i in range(24):
#     polygon(10)
#     t.left(15)
#
# move(-220,-220)
#
# for i in range(10):
#     polygon(6)
#     t.left(36)
#
# move(200,200)
#
# for i in range(6):
#     polygon(4)
#     t.left(60)
#
# move(200,-200)
#
# for i in range(6):
#     polygon(7)
#     t.left(60)
#
# move(-200,200)
#
# for i in range(60):
#     polygon(5)
#     t.left(6)


def olympic_circle(x, y, color):
    # енять цвет карандаша
    t.color(color)
    t.width(10)
    move(x, y)
    circle()


def olympic_logo():
    olympic_circle(-120, 60, "blue")
    olympic_circle(0, 60, "black")
    olympic_circle(120, 60, "red")
    olympic_circle(-60, 0, "yellow")
    olympic_circle(60, 0, "green")




def up():
    # поворот карандаша
    t.setheading(90)
    t.forward(10)


def down():
    t.setheading(-90)
    t.forward(10)


def left():
    t.setheading(180)
    t.forward(10)


def right():
    t.setheading(0)
    t.forward(10)


def up_or_down():
    # проверяет зажат ли карандаш
    if t.isdown():
        t.up()
    else:
        t.down()
def red():
    t.color("red")
#бинты
t.screen.onkeypress(up, "Up")
t.screen.onkeypress(down, "Down")
t.screen.onkeypress(left, "Left")
t.screen.onkeypress(right, "Right")
t.screen.onkeypress(up_or_down, "space")
t.screen.onkeypress(spiral, "s")
t.screen.onkeypress(red, "r")
# чтобы клавиатура слушалась
t.screen.listen()


# Рисование радуги
def rainbow():
    t.setheading(90)
    move(0, 100)
    t.width(10)
    t.color("red")
    for i in range(30):
        t.forward(7)
        t.left(6)

    move(-10, 100)
    t.setheading(90)
    t.color("orange")
    for i in range(30):
        t.forward(6)
        t.left(6)

    move(-20, 100)
    t.setheading(90)
    t.color("yellow")
    for i in range(30):
        t.forward(5)
        t.left(6)
    move(-30, 100)

    t.setheading(90)
    t.color("green")
    for i in range(30):
        t.forward(4)
        t.left(6)

    move(-40, 100)
    t.setheading(90)
    t.color("blue")
    for i in range(30):
        t.forward(3)
        t.left(6)

    move(-50, 100)
    t.setheading(90)
    t.color("purple")
    for i in range(30):
        t.forward(2)
        t.left(6)


rainbow()


t.screen.mainloop()

