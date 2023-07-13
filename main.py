
from turtle import Screen
from snake_part1 import Snake
from scoreboard import Scoreboard
from food import Food
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("MY SNAKE GAME")
screen.tracer(0)

snake_part1 = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake_part1.up,"Up")
screen.onkey(snake_part1.down,"Down")
screen.onkey(snake_part1.left,"Left")
screen.onkey(snake_part1.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake_part1.move()

    #detect collision with food.
    if snake_part1.head.distance(food) < 15:
        food.refresh()
        snake_part1.extend()
        scoreboard.increase_score()

    #detech collision with wall.
    if snake_part1.head.xcor() > 280 or snake_part1.head.xcor() < -280 or snake_part1.head.ycor() > 280 or snake_part1.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    #detect collision with tail.
    for segment in snake_part1.segments[1:]:
        if snake_part1.head.distance(segment) < 10 :
            game_is_on = False
            scoreboard.game_over()

    #if head collision with any segment in the tail:
        #trigger game_over.

screen.exitonclick()