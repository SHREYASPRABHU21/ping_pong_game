from turtle import *


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x = 10
        self.y = 10
        self.speed("fastest")
        self.move_speed = 0.1
    def move(self):
        self.goto(self.xcor() + self.x, self.ycor() + self.y)

    def bounce_y(self):
        self.y = self.y * -1

    def bounce_x(self):
        self.x = self.x * -1
        self.move_speed *= 0.8