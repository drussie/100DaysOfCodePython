from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

RIGHTPANEL_COORDINATES = (350, 0)
LEFTPANEL_COORDINATES = (-350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)  # Used with screen.update
screen.bgcolor('black')
screen.title("Pong")

r_paddle = Paddle(RIGHTPANEL_COORDINATES)
l_paddle = Paddle(LEFTPANEL_COORDINATES)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    ball.move_ball()
    time.sleep(ball.move_speed)
    screen.update()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        time.sleep(ball.move_speed)

    # detect if ball hits right wall
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_points()

    # Detect if ball hits left wall
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_points()

screen.exitonclick()
