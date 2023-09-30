from turtle import Turtle

FONT = ("Comic Sans MS", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.level = 0
        self.update_scoreboard()

    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.setpos(-290, 250)
        self.write(f"LEVEL: {self.level}", align="left", font=FONT)
