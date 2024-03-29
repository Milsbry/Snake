from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, font='Arial', font_size=14, x_position=0):
        super().__init__()
        self.font = font
        self.font_size = font_size
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.x_position = x_position
        self.goto(x_position, int((self.screen.window_height() / 2) - (font_size + 10)))  # Makes the position dynamic based
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
        if self.score > self.high_score:
            self.high_score += 1
        self.write(arg=f"Score: {self.score}   High Score: {self.high_score}", move=False, align="center", font=(self.font, self.font_size, 'normal'))

    def game_over(self):
        self.goto(0, 0)  # Game over messaging should appear in the centre of the screen
        self.write(arg=f"GAME OVER", move=False, align="center", font=(self.font, self.font_size, 'normal'))




# TODO The game can't have a hard stop anymore, everything should be reset instead
# TODO score needs to be wiped
# TODO GAME OVER needs to be wiped
# TODO Snake needs to head back to starting position
# TODO make a high score function, it should increase every time score increases It should store the highest score
#  somewhere It should compare this stored score with the current score, and update to reflect the score only if it's
#  larger than stored score
