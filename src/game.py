import tkinter as tk
from src.snake import Snake
from src.food import Food

GAME_WIDTH = 600
GAME_HEIGHT = 400
SPEED = 100
SPACE_SIZE = 20
BODY_PARTS = 3


class SnakeGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Snake Game")
        self.window.resizable(False, False)

        self.score = 0
        self.direction = "down"

        self.label = tk.Label(
            self.window, text=f"Score: {self.score}", font=("consolas", 20)
        )
        self.label.pack()

        self.canvas = tk.Canvas(
            self.window, bg="#000000", height=GAME_HEIGHT, width=GAME_WIDTH
        )
        self.canvas.pack()

        self.window.update()
        ww = self.window.winfo_width()
        wh = self.window.winfo_height()
        sw = self.window.winfo_screenwidth()
        sh = self.window.winfo_screenheight()
        self.window.geometry(f"{ww}x{wh}+{int((sw/2)-(ww/2))}+{int((sh/2)-(wh/2))}")

        self.window.bind("<Left>", lambda event: self.change_direction("left"))
        self.window.bind("<Right>", lambda event: self.change_direction("right"))
        self.window.bind("<Up>", lambda event: self.change_direction("up"))
        self.window.bind("<Down>", lambda event: self.change_direction("down"))

        self.snake = Snake(BODY_PARTS, SPACE_SIZE)
        for x, y in self.snake.coordinates:
            sq = self.canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=self.snake.color
            )
            self.snake.squares.append(sq)

        self.food = Food(GAME_WIDTH, GAME_HEIGHT, SPACE_SIZE)
        self.canvas.create_oval(
            self.food.coordinates[0],
            self.food.coordinates[1],
            self.food.coordinates[0] + SPACE_SIZE,
            self.food.coordinates[1] + SPACE_SIZE,
            fill=self.food.color,
            tag="food",
        )

        self.next_turn()

    def change_direction(self, new_direction):
        opposites = {
            "left": "right",
            "right": "left",
            "up": "down",
            "down": "up",
        }
        if new_direction != opposites.get(self.direction):
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

        self.snake.coordinates.insert(0, (x, y))
        square = self.canvas.create_rectangle(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=self.snake.color
        )
        self.snake.squares.insert(0, square)

        if x == self.food.coordinates[0] and y == self.food.coordinates[1]:
            self.score += 1
            self.label.config(text=f"Score: {self.score}")
            self.canvas.delete("food")
            self.food = Food(GAME_WIDTH, GAME_HEIGHT, SPACE_SIZE)
            self.canvas.create_oval(
                self.food.coordinates[0],
                self.food.coordinates[1],
                self.food.coordinates[0] + SPACE_SIZE,
                self.food.coordinates[1] + SPACE_SIZE,
                fill=self.food.color,
                tag="food",
            )
        else:
            del self.snake.coordinates[-1]
            self.canvas.delete(self.snake.squares[-1])
            del self.snake.squares[-1]

        if self.check_collisions():
            self.game_over()
        else:
            self.window.after(SPEED, self.next_turn)

    def check_collisions(self):
        x, y = self.snake.coordinates[0]

        if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
            return True

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
        )

    def run(self):
        self.window.mainloop()
