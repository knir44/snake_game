from turtle import Turtle

FONT = ('Courier', 24, 'normal')
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(x = -10 , y = 265)
        self.update_score()



    def update_score(self):

        self.write(f"score: {self.score}", font = FONT, align = ALIGNMENT)

    def refresh_score(self):
        self.clear()
        self.score += 1
        self.update_score()
