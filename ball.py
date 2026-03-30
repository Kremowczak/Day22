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
        self.x_move = 7
        self.y_move = 7

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def upper_wall_hit(self):
        self.y_move = -7
    def lower_wall_hit(self):
        self.y_move = 7
    def right_paddle_hit(self):
        self.x_move = -7
    def left_paddle_hit(self):
        self.x_move = 7