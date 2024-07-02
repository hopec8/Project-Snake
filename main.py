from turtle import Screen, Turtle
import time
from snake import Snake
import food
import scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SLEEP_TIME = 0.1

snake = Snake()
food = food.Food()
scoreboard = scoreboard.Scoreboard()

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(SLEEP_TIME)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall
    if abs(snake.head.xcor()) > SCREEN_WIDTH // 2-20 or abs(snake.head.ycor()) > SCREEN_HEIGHT // 2-20:
        scoreboard.reset_scoreboard()
        snake.reset_snake()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_scoreboard()
            snake.reset_snake()

screen.exitonclick()
