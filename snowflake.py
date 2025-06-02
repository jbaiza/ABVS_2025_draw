import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")

pen = turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.pensize(2)

def koch(length, level):
    if level == 0:
        pen.forward(length)
    else:
        length /= 3.0
        koch(length, level - 1)
        pen.left(60)
        koch(length, level - 1)
        pen.right(120)
        koch(length, level - 1)
        pen.left(60)
        koch(length, level - 1)

def draw_snowflake(length, level):
    for _ in range(3):
        koch(length, level)
        pen.right(120)

pen.penup()
pen.goto(-150, 100)
pen.pendown()

draw_snowflake(300, 3)  # Length, Recursion Depth (try 3 or 4)

pen.hideturtle()
screen.exitonclick()
