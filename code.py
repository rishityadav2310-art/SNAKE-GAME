import tkinter as tk
import random

# Game Configuration
GAME_WIDTH = 600
GAME_HEIGHT = 400
SPEED = 100  # Lower number = faster speed (milliseconds)
SPACE_SIZE = 20
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class Snake:
    def __init__(self, canvas):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        # Initial starting position at top-left corner
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake"
            )
            self.squares.append(square)


class Food:
    def __init__(self, canvas):
        # Generate random coordinates aligned to the grid
        x = random.randint(0, int((GAME_WIDTH / SPACE_SIZE) - 1)) * SPACE_SIZE
        y = random.randint(0, int((GAME_HEIGHT / SPACE_SIZE) - 1)) * SPACE_SIZE

        self.coordinates = [x, y]
        canvas.create_oval(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food"
        )


class SnakeGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Snake Game")
        self.window.resizable(False, False)

        self.score = 0
        self.direction = "down"

        # Score display
        self.label = tk.Label(
            self.window, text=f"Score: {self.score}", font=("consolas", 20)
        )
        self.label.pack()

        # Canvas for the game board
        self.canvas = tk.Canvas(
            self.window,
            bg=BACKGROUND_COLOR,
            height=GAME_HEIGHT,
            width=GAME_WIDTH,
        )
        self.canvas.pack()

        # Center the window on screen
        self.window.update()
        window_width = self.window.winfo_width()
        window_height = self.window.winfo_height()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Controls
        self.window.bind("<Left>", lambda event: self.change_direction("left"))
        self.window.bind("<Right>", lambda event: self.change_direction("right"))
        self.window.bind("<Up>", lambda event: self.change_direction("up"))
        self.window.bind("<Down>", lambda event: self.change_direction("down"))

        # Initialize game entities
        self.snake = Snake(self.canvas)
        self.food = Food(self.canvas)

        # Start game loop
        self.next_turn()
        self.window.mainloop()

    def change_direction(self, new_direction):
        # Prevent 180-degree turns into oneself
        if new_direction == "left" and self.direction != "right":
            self.direction = new_direction
        elif new_direction == "right" and self.direction != "left":
            self.direction = new_direction
        elif new_direction == "up" and self.direction != "down":
            self.direction = new_direction
        elif new_direction == "down" and self.direction != "up":
            self.direction = new_direction

    def next_turn(self):
        x, y = self.snake.coordinates[0]

        if self.direction == "up":
            y -= SPACE_SIZE
        elif self.direction == "down":
            y += SPACE_SIZE
        elif self.direction == "left":
            x -= SPACE_SIZE
        elif self.direction == "right":
            x += SPACE_SIZE

        # Insert new head segment
        self.snake.coordinates.insert(0, (x, y))
        square = self.canvas.create_rectangle(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR
        )
        self.snake.squares.insert(0, square)

        # Check if food is eaten
        if x == self.food.coordinates[0] and y == self.food.coordinates[1]:
            self.score += 1
            self.label.config(text=f"Score: {self.score}")
            self.canvas.delete("food")
            self.food = Food(self.canvas)
        else:
            # Remove tail segment if food wasn't eaten
            del self.snake.coordinates[-1]
            self.canvas.delete(self.snake.squares[-1])
            del self.snake.squares[-1]

        # Check for collisions
        if self.check_collisions():
            self.game_over()
        else:
            self.window.after(SPEED, self.next_turn)

    def check_collisions(self):
        x, y = self.snake.coordinates[0]

        # Wall collisions
        if x < 0 or x >= GAME_WIDTH:
            return True
        if y < 0 or y >= GAME_HEIGHT:
            return True

        # Self collisions
        for body_part in self.snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True

        return False

    def game_over(self):
        self.canvas.delete(tk.ALL)
        self.canvas.create_text(
            self.canvas.winfo_width() / 2,
            self.canvas.winfo_height() / 2,
            font=("consolas", 40),
            text="GAME OVER",
            fill="red",
            tag="gameover",
        )


if __name__ == "__main__":
    SnakeGame()
