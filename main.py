import time
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.2)
    snake.move()

#     Detect collision with food
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend()
        scoreboard.my_score()

#     Detect collision with walls
    if not((-290 < snake.head.xcor() < 290) and (-290 < snake.head.ycor() < 290)):
        game_is_on = False
        scoreboard.game_over()

#     Detect collisions with tail
    for segment in snake.segments:
        if segment != snake.head:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

screen.exitonclick()
