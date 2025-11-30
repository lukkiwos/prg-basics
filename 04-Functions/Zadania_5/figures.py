###
# Draw a square
#
import turtle

def draw_square(pen, length):
    pen = turtle.Turtle()
    pen.speed(5)
    for i in range(4):
        pen.forward(length)
        pen.right(90)


def draw_trangle(pen, length):
    pen = turtle.Turtle()
    pen.speed(5)
    for i in range(3):
        pen.forward(length)
        pen.right(120)



def draw_rectangle(length_a, length_b):
    pen = turtle.Turtle()
    pen.speed(5)
    for i in range(2):
        pen.forward(length_a)
        pen.right(90)
        pen.forward(length_b)
        pen.right(90)
    pen.hideturtle()
