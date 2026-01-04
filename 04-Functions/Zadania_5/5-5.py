###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor('purple')

# Create the turtle
pen = turtle.Turtle()
pen.speed(2)



### Draw figures

# Draw a square
def draw_square(length):
    for i in range(4):
        pen.forward(length)
        pen.right(90)

    pen.penup()
    pen.goto(-80, 0)
    pen.pendown()

    for i in range(4):
        pen.forward(length)
        pen.right(90)

    pen.penup()
    pen.goto(-200, 0)
    pen.pendown()


# Draw a trangle
def draw_trangle(length):
    
    for i in range(3):
        pen.forward(length)
        pen.right(120)

    pen.penup()
    pen.goto(-300, 0)
    pen.pendown()
    
    for i in range(3):
        pen.forward(length)
        pen.right(120)
    
    pen.penup()
    pen.goto(-300, -200)
    pen.pendown()


# Draw w rectangle
def draw_rectangle(lenght_a, lenght_b):
    for i in range(2):
        pen.forward(lenght_a)
        pen.right(90)
        pen.forward(lenght_b)
        pen.right(90)

    pen.penup()
    pen.goto(-200, -200)
    pen.pendown()

    for i in range(2):
        pen.forward(lenght_a)
        pen.right(90)
        pen.forward(lenght_b)
        pen.right(90)


    # Hide the turtle and finish
    pen.hideturtle()
    window.mainloop()


if __name__ == "__main__":
    print(draw_square(50))
    print(draw_trangle(80))
    print(draw_rectangle(40,80))