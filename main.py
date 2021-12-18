from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
x = 0
y = 0

for segment in range(0, 3):
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(x=x, y=y)
    x -= 20
    y = y

screen.exitonclick()
