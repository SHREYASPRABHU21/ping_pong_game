from turtle import *

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(100, 220)
        self.write(f"{self.r_score}",font=("Arial",50,"normal"))
        self.goto(-100,220)
        self.write(f"{self.l_score}",font=("Arial",50,"normal"))

    def r_update(self):
        self.r_score += 1
        self.update()

    def l_update(self):
        self.l_score += 1
        self.update()

