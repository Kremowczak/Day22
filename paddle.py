from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(x,y=0)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.forward(-20)
