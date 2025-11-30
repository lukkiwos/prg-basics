import turtle
import figures

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

# --- Draw figures ---

# 1. KWADRAT
# Pozycja 1: Gdzieś na lewo u góry
pen.penup() 
pen.goto(-150, 150) # Przenieś żółwia bez rysowania
pen.pendown()
figures.draw_square(pen, 50) # Rysowanie kwadratu o boku 50

# Pozycja 2: Gdzieś na prawo na dole
pen.penup()
pen.goto(100, -100)
pen.setheading(0) # Zresetuj kierunek (opcjonalne, ale dobre praktycznie)
pen.pendown()
figures.draw_square(pen, 80) # Rysowanie kwadratu o boku 80

# 2. TRÓJKĄT
# Pozycja 1: Na środku u góry
pen.penup()
pen.goto(0, 150)
pen.setheading(0) 
pen.pendown()
figures.draw_triangle(pen, 70) 

# Pozycja 2: Na środku na dole
pen.penup()
pen.goto(-50, -150)
pen.setheading(0) 
pen.pendown()
figures.draw_triangle(pen, 100) 

# 3. PROSTOKĄT
# Pozycja 1: Lewo na dole
pen.penup()
pen.goto(-200, -50)
pen.setheading(0)
pen.pendown()
figures.draw_rectangle(pen, 120, 50) # Rysowanie 120x50

# Pozycja 2: Prawo na górze
pen.penup()
pen.goto(150, 50)
pen.setheading(0) 
pen.pendown()
figures.draw_rectangle(pen, 90, 40) # Rysowanie 90x40

# --- Hide the turtle and finish ---
pen.hideturtle()
window.mainloop()

