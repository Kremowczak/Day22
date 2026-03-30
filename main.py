from turtle import Screen
from paddle import Paddle
from ball import Ball
import time



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



while game_on:
    ball.move()
    screen.update()
    time.sleep(0.1)







screen.exitonclick()



