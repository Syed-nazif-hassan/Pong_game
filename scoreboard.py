from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.l_paddle = 0
        self.r_paddle = 0
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 260)
        self.write(arg=self.l_paddle, align="center", font=("Arial", 20, "italic"))
        self.goto(100, 260)
        self.write(arg=self.r_paddle, align="center", font=("Arial", 20, "italic"))

    def l_score(self):
        self.l_paddle += 1
        self.update_score()

    def r_score(self):
        self.r_paddle += 1
        self.update_score()
