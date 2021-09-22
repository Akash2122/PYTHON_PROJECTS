from turtle import Screen
import time
from snake import Snake
from food import Food
from score import ScoreBoard
import winsound


GAME_IS_ON = True

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game by Akash")
screen.tracer(0)

snake=Snake()
food =Food()
score=ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while GAME_IS_ON:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.head.distance(food) < 15:
        winsound.PlaySound('food.wav',winsound.SND_ASYNC)
        food.create_food()
        score.increase_score()
        snake.extend_segment()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        GAME_IS_ON = False
        winsound.PlaySound('gameover.wav',winsound.SND_ASYNC)
        score.game_over()
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            winsound.PlaySound('gameover.wav',winsound.SND_ASYNC)
            GAME_IS_ON=False
            score.game_over()
            
    
screen.exitonclick()
