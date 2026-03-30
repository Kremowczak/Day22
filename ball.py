from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.x = self.xcor()
        self.y = self.ycor()
        self.x_move = 25
        self.y_move = 25

    def move(self):
        if self.ycor() >= 0:
            self.goto(self.x + self.x_move, self.y - self.y_move)
