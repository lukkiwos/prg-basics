###
# Draw a square
#
import turtle

def draw_square(length):
    for x in range(4):
        turtle.forward(length)
        turtle.right(90)

def draw_triangle(length):
    for x in range(3):
        turtle.forward(length)
        turtle.right(120)

def draw_rectangle(length_a, length_b):
    for x in range(2):
        turtle.forward(length_a)
        turtle.right(90)
        turtle.forward(length_b)
        turtle.right(90)