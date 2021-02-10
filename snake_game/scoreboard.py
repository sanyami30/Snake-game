from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        self.score = 0
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 20, "normal"))

    def update_scoreboard(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over.", align="center", font=("Courier", 20, "normal"))
