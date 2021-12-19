from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        with open("data.txt") as scores:
            self.high_score = int(scores.read())
        self.goto(0, 260)
        self.color("White")
        self.my_score()
        self.hideturtle()

    def my_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High score: {self.high_score}", align="center", font=('Courier', 20, 'normal'))
        self.score += 1

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as scores:
                scores.write(f"{self.high_score}")
        self.score = 0


