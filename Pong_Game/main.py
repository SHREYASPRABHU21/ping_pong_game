from turtle import *
from paddle import *
from ball import *
import time
from Scoreboard import *

screen = Screen()
screen.setup(width = 1000, height = 600)
screen.title("Ping_Pong")
screen.bgcolor("black")
screen.tracer(0)
scoreboard = Scoreboard()
ball = Ball()
l_paddle = Paddle((-480,10))
r_paddle = Paddle((480,10))
screen.listen()

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down,"s")


screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down,"Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 460 and ball.distance(r_paddle) < 40 or ball.xcor() < -460 and ball.distance(l_paddle) < 40:
        ball.bounce_x()


    if ball.xcor() > 500 and ball.distance(r_paddle) > 40:
        time.sleep(1)
        ball.goto(0,0)
        ball.bounce_x()
        scoreboard.l_update()
        ball.move_speed = 0.1

    if ball.xcor() < -500 and ball.distance(l_paddle) > 40:
        time.sleep(1)
        ball.goto(0, 0)
        ball.bounce_x()
        scoreboard.r_update()
        ball.move_speed = 0.1










screen.exitonclick()