from turtle import Turtle, Screen
import random


# Our food class inherits everything from the turtle class
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")  # Our food should be a circle
        self.penup()  # Creates a 10 X 10 circle
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")  # Food should move to destination on the screen quickly
        self.speed("fastest")

        # Set up the screen so that the first bit of food appears dynamically, whatever the size of the screen
        self.refresh_food()

    def refresh_food(self):
        """Resets the food to a new coordinate dynamically depending on the screen size"""
        self.screen = Screen()
        self.random_x = random.randint(-int(self.screen.window_width() / 2 - 20),
                                       int(self.screen.window_width() / 2 - 20))
        self.random_y = random.randint(-int(self.screen.window_height() / 2 - 20),
                                       int(self.screen.window_height() / 2 - 20))
        self.goto(self.random_x, self.random_y)
