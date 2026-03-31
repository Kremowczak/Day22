from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.penup()
        self.speed(0)
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=8)

    def draw_line(self):
        self.goto(0, 300)
        self.setheading(270)
        for i in range(18):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    def add_score1(self):
        self.score1 += 1