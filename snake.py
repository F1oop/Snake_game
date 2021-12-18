from turtle import Turtle


class Snake:
    starting_positions = [(0, 0), (-20, 0), (-40, 0)]
    segments = []

    for position in starting_positions:
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        segments.append(new_segment)

    def move(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(x=self.segments[seg_num - 1].xcor(), y=self.segments[seg_num - 1].ycor())
        self.segments[0].forward(20)