from turtle import Screen
from Snake import Snake
import time
from Food import Food
from scoreboard import ScoreBoard

sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("black")
sc.tracer(0)
sc.title("Snake Game")


snake = Snake()
food = Food()
scores = ScoreBoard()


sc.listen()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.left, "Left")
sc.onkey(snake.right, "Right")

game = True
while game:
    sc.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scores.update_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game = False
        scores.game_over()

    for segments in snake.turtle_list[1:]:
        if snake.head.distance(segments) < 10:
            game = False
            scores.game_over()


sc.exitonclick()
