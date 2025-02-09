from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")
screen.onkey(screen.bye, "Escape")

game_is_on = True

# Opening high score file and updating the high score:
try:
    with open("high_score.txt", mode="r") as file:
        high_score = file.read()
        if high_score.isdigit():
            scoreboard.high_score = int(high_score)
        else:
            scoreboard.high_score = 0
        scoreboard.reset()
except FileNotFoundError:
    scoreboard.high_score = 0

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Food collision detection:
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Tail collision detection:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            with open("high_score.txt", mode="w") as file:
                file.write(str(scoreboard.high_score))
            time.sleep(1)

    # Wall collision detection:
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        with open("high_score.txt", mode="w") as file:
            file.write(str(scoreboard.high_score))
        time.sleep(1)

scoreboard.game_over()


screen.exitonclick()
