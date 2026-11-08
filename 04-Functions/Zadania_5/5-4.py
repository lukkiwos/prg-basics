import turtle
import figures

window = turtle.Screen()
window.bgcolor("lightgreen")
turtle.speed(5)

figures.draw_square(50)

turtle.hideturtle()
window.mainloop()