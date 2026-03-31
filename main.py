from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


score_board = Scoreboard()
game_on = True
ball = Ball()
screen = Screen()
paddle = Paddle(-380)
paddle2 = Paddle(380)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()


screen.onkeypress(paddle.move_up, "w")
screen.onkeypress(paddle.move_down, "s")
screen.onkeypress(paddle2.move_up, "Up")
screen.onkeypress(paddle2.move_down, "Down")
score_board.draw_line()
score_board.draw_score()

while game_on:
    ball.move()
    screen.update()
    time.sleep(0.1)

    #colision with wall detection
    if ball.ycor() >= 280:
        ball.upper_wall_hit()
    if ball.ycor() <= -280:
        ball.lower_wall_hit()

    #collision with paddle detection
    if ball.xcor() >= (paddle2.xcor() - 20) and (paddle2.ycor()-50) <= ball.ycor() <= (paddle2.ycor() + 50):
        ball.right_paddle_hit()
    elif ball.xcor() >= (paddle2.xcor()):
        score_board.add_score1()
        score_board.draw_score()
        ball.reset_ball()
    elif ball.xcor() <= (paddle.xcor()):
        score_board.add_score2()
        score_board.draw_score()
        ball.reset_ball()
    elif ball.xcor() <= (paddle.xcor() + 20) and (paddle.ycor() -50) <=ball.ycor() <= (paddle.ycor() + 50):
        ball.left_paddle_hit()


screen.exitonclick()



