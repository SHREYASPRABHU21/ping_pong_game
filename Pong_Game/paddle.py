from turtle import *

# COR = [40,20,0,-20]

class Paddle(Turtle):
    def __init__(self,cor):
        super().__init__()
        self.create_paddle(cor)
    #
    # def create_paddle(self):
    #     for cor in COR:
    #         new_segment = Turtle()
    #         new_segment.color("white")
    #         new_segment.shape("square")
    #         new_segment.penup()
    #         new_segment.goto(480,cor)
    #         self.segments.append(new_segment)
    #     self.segments[0].left(90)
    #     self.segments[3].right(90)
    #
    # def move_up(self):
    #     for i in range(3,0,-1):
    #         self.segments[i].goto(self.segments[i-1].position())
    #
    #     self.segments[0].forward(20)
    #
    # def move_down(self):
    #     for i in range(0,3):
    #         self.segments[i].goto(self.segments[i+1].position())
    #
    #     self.segments[3].forward(20)

    def create_paddle(self,cor):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=4,stretch_len=0.5)
        self.goto(cor)

    def move_up(self):
        self.goto(self.xcor(),self.ycor()+20)


    def move_down(self):
        self.goto(self.xcor(),self.ycor()-20)
