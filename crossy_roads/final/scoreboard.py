from turtle import Turtle, home

class Scoreboard(Turtle):

    font = ("Menlo", 18, "normal")

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.goto(-230, 220)
        self.score_display()

    def score_display(self):
        self.clear()
        self.write(f"Level: {self.level}", align = "left", font = self.font)

    def increase_level(self):
        self.level += 1
        self.score_display()

    def game_over(self):
        self.home() # origin
        self.write(f"GAME OVER", align = "center", font = self.font)