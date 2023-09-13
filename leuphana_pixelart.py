import turtle
from leuphana_pixelcolors import get_matrix

turtle.Screen().setup(width=750, height=550, startx=0, starty=0)

t = turtle.Turtle()
t.speed(0)
turtle.tracer(0)  # This turns off the animation, because otherwise it would take too long to generate.
t.penup()
t.goto(-350, -240)
t.pendown()

side_length = 5


def create_square(t, side_length, color):
    t.color(color)
    t.begin_fill()
    for num in range(4):
        t.forward(side_length)
        t.right(90)
    t.end_fill()
    t.forward(side_length)


color_matrix = get_matrix()[::-1]


def create_row(t, side_length, color_list):
    t.penup()
    t.left(90)
    t.forward(side_length)
    t.left(90)
    t.forward(side_length * len(color_list))
    t.right(180)
    t.pendown()

# l stands for each list in the matrix, c stands for each color in each list.

for l in color_matrix:
    for c in l:
        create_square(t, side_length, c)
        turtle.update()  # This makes the animation of the Turtle periodically visible again.
    create_row(t, side_length, l)


turtle.done()
