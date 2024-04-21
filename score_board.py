from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, font='Arial', font_size=14, x_position=0):
        super().__init__()
        self.font = font
        self.font_size = font_size
        self.score = 0
        with open("data.txt", mode="r") as high_score_data: # we need to convert the saved score to an int
            self.high_score = int(high_score_data.read())

        self.penup()
        self.hideturtle()
        self.color("white")
        self.x_position = x_position
        self.goto(x_position,
                  int((self.screen.window_height() / 2) - (font_size + 10)))  # Makes the position dynamic based
        # on font size
        self.update_scoreboard()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        self.clear()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard with current score."""
        self.goto(self.x_position, int((self.screen.window_height() / 2) - (self.font_size + 10)))
        self.high_score = int(self.high_score)
        if self.score > self.high_score:
            self.high_score += 1
            self.high_score = str(self.high_score)
            with open("data.txt", mode="w") as high_score_data: # here we write the high score to a text file
                high_score_data.write(f"{self.high_score}")
        self.write(arg=f"Score: {self.score}   High Score: {self.high_score}", move=False, align="center",
                   font=(self.font, self.font_size, 'normal')) # writing the scores to the screen

    def game_over(self):
        self.goto(0, 0)  # Game over messaging should appear in the centre of the screen
        self.write(arg=f"GAME OVER", move=False, align="center", font=(self.font, self.font_size, 'normal'))


