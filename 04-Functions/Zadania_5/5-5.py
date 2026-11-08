###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
import figures
import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

## Draw figures
turtle.penup()
turtle.goto(-300,300)
turtle.pendown()
figures.draw_square(50)

turtle.penup()
turtle.goto(-300,100)
turtle.pendown()
figures.draw_square(70)

turtle.penup()
turtle.goto(-300,-100)
turtle.pendown()
figures.draw_triangle(80)

turtle.penup()
turtle.goto(200,300)
turtle.pendown()
figures.draw_triangle(60)

turtle.penup()
turtle.goto(200,100)
turtle.pendown()
figures.draw_rectangle(40,60)

turtle.penup()
turtle.goto(200,-200)
turtle.pendown()
figures.draw_rectangle(100,150)

turtle.penup()
turtle.goto(0,0)

# Hide the turtle and finish
turtle.hideturtle()
window.mainloop()