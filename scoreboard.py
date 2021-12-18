from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.goto(0, 260)
        self.color("White")
        self.my_score()
        self.hideturtle()

    def my_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Courier', 20, 'normal'))
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=('Courier', 40, 'normal'))