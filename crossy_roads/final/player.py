import turtle as turtle_module # typealalias
import theme

class Player(turtle_module.Turtle):

    def __init__(self):
        super().__init__()
        self.setheading(90) # initial turtle heading upward (north)
        self.shape("turtle")
        self.color(theme.Theme.shiny_shamrock)
        self.penup() # does not draw a line with pen
        self.goto_start()

    def move(self):
        self.forward(10)

    def goto_start(self):
        self.goto(x = 0, y = -230) # Toni's start position from the bottom

    def cross_finish_line(self):
        if self.ycor() > 250:
            return True
        else:
            return False