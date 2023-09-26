from turtle import Screen, Turtle
import time
from food import Food
from score_board import ScoreBoard

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
        self.score_board = ScoreBoard()  # Creates a scoreboard instance as an object
        self.score_board.update_scoreboard()  # Creates the physical score board on the screen
        self.current_segment = None
        self.game_on = True
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
        print(self.position)
        self.current_segment = Turtle("square")
        self.current_segment.penup()
        self.current_segment.goto(position)  # TODO figure out why this line is breaking the code
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

    def snake_game(self):
        """While the game is on, the all 'body' segments move to the position of the one before it in the list
        (therefore in front) visually. The only exception is the head, which takes a new heading."""
        while self.game_on:
            self.screen.update()  # Ensures that the screen only updates after every segment has moved
            for segment in range(len(self.seg_list) - 1, 0, -1):
                new_x = self.seg_list[segment - 1].xcor()
                new_y = self.seg_list[segment - 1].ycor()
                self.seg_list[segment].goto(new_x, new_y)
            self.seg_list[0].forward(20)

            # Detects collision with food (from the Food class)
            # TODO eventually change the below size so it's dynamic once food has been made modular
            if self.head.distance(self.food) < 15:
                self.food.refresh_food()  # Food takes on a new position
                self.extend()  # Snake gains a new segment
                self.score_board.increase_score()  # Updates the score

            time.sleep(self.speed)

            if (
                    self.head.xcor() > (int(self.screen.window_width() / 2 - 10)) or
                    self.head.xcor() < (-int(self.screen.window_width() / 2 - 10)) or
                    self.head.ycor() > (int(self.screen.window_height() / 2 - 10)) or
                    self.head.ycor() < (-int(self.screen.window_height() / 2 - 10))
            ):
                self.game_on = False  # Collision with wall, end the game
                self.score_board.game_over()

            # Detects collision between snake head and current segment
            # Must bypass head segment, otherwise gameover will always trigger
            for segment in self.seg_list:
                if segment == self.head:
                    pass
                elif self.head.distance(segment) < 10:
                    self.game_on = False
                    self.score_board.game_over()