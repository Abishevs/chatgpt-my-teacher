import random
import time
import keyboard
import collections


class Board:
    def __init__(self, width: int, height: int, speed: float):
        self.WIDTH = width
        self.HEIGHT = height
        self.SPEED = speed
        self.board = self.__create_board()

    def __create_board(self) -> list:
        return [["□" for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]

    def print_board(self) -> None:
        print('\n')
        for row in self.board:
            print(row)


class Snake:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.head_pos = [self.x_pos, self.y_pos]

        self.body_segments = collections.deque()  # doubly end operations, faster than lists
        self.length = 0
        self.apple_pos = [0, 0]
        self.coords = [0, 0]
        self.ate = False
        self.direction = 'up'
        self.spawn_apple()

    def set_empty_square(self) -> None:
        board_obj.board[self.y_pos][self.x_pos] = "□"

    def set_head(self) -> None:
        board_obj.board[self.y_pos][self.x_pos] = "■"

    def draw_body(self) -> None:
        self.body_segments.appendleft(self.coords)
        board_obj.board[self.body_segments[0][1]][self.body_segments[0][0]] = "&"
        if not self.ate:
            board_obj.board[self.body_segments[self.length][1]][self.body_segments[self.length][0]] = "□"
            self.set_head()
            self.body_segments.pop()

    def move(self) -> None:
        self.coords = [self.x_pos, self.y_pos]
        self.set_empty_square()

        if self.direction == "right":
            self.x_pos += 1
        if self.direction == "left":
            self.x_pos -= 1
        if self.direction == "up":
            self.y_pos -= 1
        if self.direction == "down":
            self.y_pos += 1

        self.set_head()
        if self.length >= 1:
            self.draw_body()

        self.head_pos = [self.x_pos, self.y_pos]

    def spawn_apple(self) -> None:
        x = random.randint(0, board_obj.WIDTH-2)
        y = random.randint(0, board_obj.HEIGHT-2)
        apple_pos = [x, y]
        if apple_pos in self.body_segments or apple_pos == self.head_pos:
            self.spawn_apple()  # if apple spawned in snake, then run func again with recursion and quit current func
            return
        self.apple_pos = [x, y]
        board_obj.board[y][x] = "●"

    def eat_apple(self) -> None:
        self.length += 1
        self.ate = True

    def collision(self) -> bool:
        return self.head_pos in self.body_segments or self.y_pos in [board_obj.HEIGHT-1, -1] \
                or self.x_pos in [board_obj.WIDTH-1, -1]


def on_press(_: None):
    for code in keyboard._pressed_events:
        if code == 105:
            snake.direction = 'left'
        elif code == 106:
            snake.direction = 'right'
        elif code == 103:
            snake.direction = 'up'
        elif code == 108:
            snake.direction = 'down'


def start_game(snake: Snake, board_obj: Board):
    snake.set_head()
    board_obj.print_board()
    keyboard.hook(on_press)
    while not snake.collision():
        print("SNAKE: ", snake.head_pos)
        print("BODY: ", snake.body_segments)
        print("APPLE: ", snake.apple_pos)

        snake.move()
        board_obj.print_board()
        snake.ate = False
        if snake.head_pos == snake.apple_pos:
            snake.eat_apple()
            snake.spawn_apple()
        time.sleep(board_obj.SPEED)
    print(f"Game over! Points: {snake.length}")


if __name__ == "__main__":
    board_obj = Board(8, 8, 0.3)  # Set: width, height, speed
    snake = Snake(int(board_obj.WIDTH / 2), int(board_obj.HEIGHT / 2))  # Set: snake x and y position

    start_game(snake, board_obj)
