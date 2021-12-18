from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("red")
        self.speed(0)
        self.refresh()

    def refresh(self):
        rnd_x = random.randrange(-280, 280, 20)
        rnd_y = random.randrange(-280, 280, 20)
        self.goto(x=rnd_x, y=rnd_y)