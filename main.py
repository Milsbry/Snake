from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time
import tkinter as tk
from tkinter import messagebox as mb


def restart_question():
    """Shows a dialog box when the game ends, the players choice should be returned so that it can be stored."""
    return mb.askyesno(title='The game has ended', message="Would you like to play another game?")


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Amelia's Snake Game")

# Create an instance of the Snake class
snake = Snake()
food = Food()
score_board = ScoreBoard()

# We want the user to be able to restart the game if they want


game_on = True
# Get the snake game to begin


while game_on:
    snake.screen.update()  # Ensures that the screen only updates after every segment has moved
    for segment in range(len(snake.seg_list) - 1, 0, -1):
        new_x = snake.seg_list[segment - 1].xcor()
        new_y = snake.seg_list[segment - 1].ycor()
        snake.seg_list[segment].goto(new_x, new_y)
    snake.seg_list[0].forward(20)

    # Detects collision with food (from the Food class)
    # TODO eventually change the below size so it's dynamic once food has been made modular
    if snake.head.distance(food) < 15:
        food.refresh_food()  # Food takes on a new position
        snake.extend()  # Snake gains a new segment
        score_board.increase_score()  # Updates the score
    # snake.score_board.update_high_score() # Checks whether the high score should be updated

    time.sleep(snake.speed)

    if (
            snake.head.xcor() > (int(screen.window_width() / 2 - 10)) or
            snake.head.xcor() < (-int(screen.window_width() / 2 - 10)) or
            snake.head.ycor() > (int(screen.window_height() / 2 - 10)) or
            snake.head.ycor() < (-int(screen.window_height() / 2 - 10))
    ):
        # Collision with wall, end the game
        score_board.reset_score()
        play_again = restart_question()  # Stores the players output in a variable
        if play_again:
            snake.reset()
        else:
            score_board.game_over()
            game_on = False

    # Detects collision between snake head and current segment
    # Must bypass head segment, otherwise game over will always trigger
    for segment in snake.seg_list[1:]:
        if snake.head.distance(segment) < 10:
            play_again = restart_question()  # Stores the players output in a variable
            if play_again:
                snake.reset()
            else:
                game_on = False
                score_board.game_over()
                break

# Screen now only exits when player clicks
screen.exitonclick()
