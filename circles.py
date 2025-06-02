import time
import turtle

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.color("cyan")

for _ in range(36):
    pen.circle(100)
    pen.left(10)
    # time.sleep(0.5)

pen.hideturtle()
screen.exitonclick()
