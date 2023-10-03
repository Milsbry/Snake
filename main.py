from turtle import Screen
from snake import Snake


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Amelia's Snake Game")

# Create an instance of the Snake class
snake = Snake()

# Get the snake game to begin
snake.snake_game()

# Screen now only exits when player clicks
screen.exitonclick()
