from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

screen.listen()
screen.onkey(right_paddle.paddle_down, "Down")
screen.onkey(right_paddle.paddle_up, "Up")
screen.onkey(left_paddle.paddle_down, "s")
screen.onkey(left_paddle.paddle_up, "w")
game_on = True
while game_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if right_paddle.distance(ball) < 60 and ball.xcor() > 320:
        ball.bounce_x()
    if left_paddle.distance(ball) < 60 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 400:
        scoreboard.l_score()
        ball.restart()
    if ball.xcor() < -400:
        scoreboard.r_score()
        ball.restart()

screen.exitonclick()
