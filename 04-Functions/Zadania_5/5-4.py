###
# Draw a square
#
def draw_square(length):
    import turtle

    window = turtle.Screen()
    window.bgcolor('purple')

    pen = turtle.Turtle()
    pen.speed(2)

    for i in range(4):
        pen.forward(length)
        pen.right(90)

    pen.hideturtle()
    window.mainloop()


if __name__ == "__main__":
    print(draw_square(50))