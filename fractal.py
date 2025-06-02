import turtle

# Setup
screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.color("brown")
pen.speed(0)  # Fastest drawing
pen.left(90)  # Point turtle upwards
pen.penup()
pen.goto(0, -250)
pen.pendown()

# Recursive function to draw branches
def draw_branch(length):
    if length < 5:
        return
    pen.forward(length)
    pen.left(45)
    draw_branch(length - 18)
    pen.right(90)
    draw_branch(length - 18)
    pen.left(45)
    pen.backward(length)

# Draw tree
draw_branch(100)

# Exit on click
screen.exitonclick()