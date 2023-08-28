from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def paddle_down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)

    def paddle_up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)