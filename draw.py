import turtle

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.color("cyan")

for i in range(100):
    pen.forward(i * 3)
    pen.right(45)
    pen.pensize(i / 20 + 1)

pen.hideturtle()
screen.exitonclick()
