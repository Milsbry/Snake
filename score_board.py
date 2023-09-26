from turtle import Turtle, Screen


class ScoreBoard(Turtle):
    def __init__(self, font='Arial', font_size=14):
        super().__init__()
        self.font = font
        self.font_size = font_size
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, (int((self.screen.window_height() / 2) - (font_size + 10))))  # Makes the position dynamic based
        # on font size
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=(self.font, self.font_size, 'normal'))
        self.update_scoreboard()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=(self.font, self.font_size, 'normal'))

    def game_over(self):
        self.goto(0, 0) # Game over messaging should appear in the centre of the screen
        self.write(arg=f"GAME OVER", move=False, align="center", font=(self.font, self.font_size, 'normal'))

