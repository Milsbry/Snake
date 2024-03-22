from turtle import Screen, Turtle
import time
from food import Food

# Creating constants for the snake head direction
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self, n_segments=3, start_coordinates=(0, 0), seg_list=None, snake_colour="white", speed=0.1):
        """Creates any number of 'turtles' as new segments and sets them up in a line, so they can function as a
        snake for the snake mobile game"""
        self.screen = Screen()
        self.current_segment = None
        self.n_segments = n_segments
        self.screen.tracer(0)  # Stops the turtles animations until screen.refresh is called
        if seg_list is None:
            seg_list = []
        self.seg_list = seg_list
        self.speed = speed
        self.snake_colour = snake_colour
        self.x, self.y = start_coordinates
        self.create_snake()  # Create snake as default upon initialisation
        self.head = self.seg_list[0]
        self.food = Food()

        # The below has the screen await an input, the keys are bound to the respective function that changes the snake
        # direction. this has to happen under init for the snake object created here to be linked correctly
        self.screen.listen()
        self.screen.onkey(fun=self.up, key="Up")
        self.screen.onkey(fun=self.down, key="Down")
        self.screen.onkey(fun=self.left, key="Left")
        self.screen.onkey(fun=self.right, key="Right")

    def create_snake(self):
        """Creates a new snake, the number of turtle segments in the snake is determined in the initialisation of the
        class."""
        for position in range(self.n_segments):
            self.add_segment((self.x, self.y)) # segments go to the starting coordinates
            self.x -= 20  # The next segment should be next to the first, move it along the width of the segment

    def add_segment(self, position):
        """Adds a new segment in the snake, can be used when the snake is being created for the first time, or when the
        snake needs to be extended."""
        self.position = position
        self.current_segment = Turtle("square")
        self.current_segment.penup()
        self.current_segment.goto(position)
        self.current_segment.color(self.snake_colour)
        self.seg_list.append(self.current_segment)

    def extend(self):
        """Extend the snake when the player score increases"""
        last_segment_position = self.seg_list[-1].position()
        self.add_segment(last_segment_position)
        # -1 indicates that we should add a segment to the END of the list.
        # The segment takes on the exact position of the last segment in the list. This works due to functionality
        # built into the snake_game method. The segments all move to the current position of the previous segment in
        # the list (excluding the snake head), this means the second to last segment will move, but the last segment
        # Will not. When the screen refreshes this means the segments will be in a line.

    # The functions below dictate how the head of the snake moves, the heading method returns the snakes current heading
    # the if statements ensure the snake cannot turn in the opposite direction that it's currently going.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)



