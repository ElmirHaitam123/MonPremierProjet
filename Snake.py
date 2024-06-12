import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.root.geometry("640x480")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, bg="black", height=480, width=640)
        self.canvas.pack()

        self.score = 0
        self.game_over = False
        self.snake = []
        self.food = None

        self.init_game()
        self.root.bind("<KeyPress>", self.change_direction)
        
        self.replay_button = tk.Button(self.root, text="Rejouer", command=self.init_game)
        self.replay_button.pack()
        
        self.update_snake()

    def init_game(self):
        self.canvas.delete("all")
        self.score = 0
        self.game_over = False
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.snake_dir = "Right"
        self.food = self.create_food()
        self.draw_food()
        self.draw_snake()

    def create_food(self):
        x = random.randint(0, 63) * 10
        y = random.randint(0, 47) * 10
        return x, y

    def draw_food(self):
        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0] + 10, self.food[1] + 10, fill="red", tag="food")

    def draw_snake(self):
        self.canvas.delete("snake")
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0] + 10, segment[1] + 10, fill="green", tag="snake")

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.snake_dir == "Up":
            new_head = (head_x, head_y - 10)
        elif self.snake_dir == "Down":
            new_head = (head_x, head_y + 10)
        elif self.snake_dir == "Left":
            new_head = (head_x - 10, head_y)
        elif self.snake_dir == "Right":
            new_head = (head_x + 10, head_y)

        self.snake = [new_head] + self.snake[:-1]

        if self.snake[0] == self.food:
            self.snake.append(self.snake[-1])
            self.food = self.create_food()
            self.canvas.delete("food")
            self.draw_food()
            self.score += 1

    def check_collision(self):
        head_x, head_y = self.snake[0]
        if not (0 <= head_x < 640 and 0 <= head_y < 480):
            self.game_over = True
        if len(self.snake) != len(set(self.snake)):
            self.game_over = True

    def update_snake(self):
        if not self.game_over:
            self.move_snake()
            self.draw_snake()
            self.check_collision()
            self.root.after(100, self.update_snake)
        else:
            self.canvas.create_text(320, 240, text="Game Over", fill="white", font=("Helvetica", 36))

    def change_direction(self, event):
        new_dir = event.keysym
        all_directions = {
            "z": "Up", "s": "Down", "q": "Left", "d": "Right"
        }

        if new_dir in all_directions:
            if (self.snake_dir == "Up" and new_dir != "s") or \
               (self.snake_dir == "Down" and new_dir != "z") or \
               (self.snake_dir == "Left" and new_dir != "d") or \
               (self.snake_dir == "Right" and new_dir != "q"):
                self.snake_dir = all_directions[new_dir]

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
