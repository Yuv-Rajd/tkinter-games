from tkinter import *
import random
import time
import numpy as np
from PIL import ImageTk,Image

# Define useful parameters
size_of_board = 600
rows = 10
cols = 10
DELAY = 100
snake_initial_length = 3
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 2
RED_COLOR = "#EE4035"
BLUE_COLOR = "#0492CF"
Green_color = "#7BC043"

BLUE_COLOR_LIGHT = '#67B0CF'
RED_COLOR_LIGHT = '#EE7E77'




def initialize_board():
    board = []
    apple_obj = []
    old_apple_cell = []

    for i in range(rows):
        for j in range(cols):
            board.append((i, j))

    for i in range(rows):
        canvas.create_line(
            i * size_of_board / rows, 0, i * size_of_board / rows, size_of_board,
        )

    for i in range(cols):
        canvas.create_line(
            0, i * size_of_board / cols, size_of_board, i * size_of_board / cols,
        )

def initialize_snake():
    snake = []
    crashed = False
    snake_heading = "Right"
    last_key = snake_heading
    forbidden_actions = {}
    forbidden_actions["Right"] = "Left"
    forbidden_actions["Left"] = "Right"
    forbidden_actions["Up"] = "Down"
    forbidden_actions["Down"] = "Up"
    snake_objects = []
    for i in range(snake_initial_length):
        snake.append((i, 0))

def play_again():
    canvas.delete("all")
    initialize_board()
    initialize_snake()
    place_apple()
    display_snake(mode="complete")
    begin_time = time.time()

def mainloop():
    while True:
        window.update()
        if begin:
            if not crashed:
                window.after(DELAY, update_snake(last_key))
            else:
                begin = False
                display_gameover()

# ------------------------------------------------------------------
# Drawing Functions:
# The modules required to draw required game based object on canvas
# ------------------------------------------------------------------
def display_gameover():
    score = len(snake)
    canvas.delete("all")
    score_text = "Scores \n"

    # put gif image on canvas
    # pic's upper left corner (NW) on the canvas is at x=50 y=10

    canvas.create_text(
        size_of_board / 2,
        3 * size_of_board / 8,
        font="cmr 40 bold",
        fill=Green_color,
        text=score_text,
    )
    score_text = str(score)
    canvas.create_text(
        size_of_board / 2,
        1 * size_of_board / 2,
        font="cmr 50 bold",
        fill=BLUE_COLOR,
        text=score_text,
    )
    time_spent = str(np.round(time.time() - begin_time, 1)) + 'sec'
    canvas.create_text(
        size_of_board / 2,
        3 * size_of_board / 4,
        font="cmr 20 bold",
        fill=BLUE_COLOR,
        text=time_spent,
    )
    score_text = "Click to play again \n"
    canvas.create_text(
        size_of_board / 2,
        15 * size_of_board / 16,
        font="cmr 20 bold",
        fill="gray",
        text=score_text,
    )

def place_apple():
    # Place apple randomly anywhere except at the cells occupied by snake
    unoccupied_cels = set(board) - set(snake)
    apple_cell = random.choice(list(unoccupied_cels))
    row_h = int(size_of_board / rows)
    col_w = int(size_of_board / cols)
    x1 = apple_cell[0] * row_h
    y1 = apple_cell[1] * col_w
    x2 = x1 + row_h
    y2 = y1 + col_w
    apple_obj = canvas.create_rectangle(
        x1, y1, x2, y2, fill=RED_COLOR_LIGHT, outline=BLUE_COLOR,
    )

def display_snake(mode=""):
    # Remove tail from display if it exists
    if snake_objects != []:
        canvas.delete(snake_objects.pop(0))
    if mode == "complete":
        for i, cell in enumerate(snake):
            # print(cell)
            row_h = int(size_of_board / rows)
            col_w = int(size_of_board / cols)
            x1 = cell[0] * row_h
            y1 = cell[1] * col_w
            x2 = x1 + row_h
            y2 = y1 + col_w
            snake_objects.append(
                canvas.create_rectangle(
                    x1, y1, x2, y2, fill=BLUE_COLOR, outline=BLUE_COLOR,
                )
            )
    else:
        # only update head
        cell = snake[-1]
        row_h = int(size_of_board / rows)
        col_w = int(size_of_board / cols)
        x1 = cell[0] * row_h
        y1 = cell[1] * col_w
        x2 = x1 + row_h
        y2 = y1 + col_w
        snake_objects.append(
            canvas.create_rectangle(
                x1, y1, x2, y2, fill=BLUE_COLOR, outline=RED_COLOR,
            )
        )
        if snake[0] == old_apple_cell:
            snake.insert(0, old_apple_cell)
            old_apple_cell = []
            tail = snake[0]
            row_h = int(size_of_board / rows)
            col_w = int(size_of_board / cols)
            x1 = tail[0] * row_h
            y1 = tail[1] * col_w
            x2 = x1 + row_h
            y2 = y1 + col_w
            snake_objects.insert(
                0,
                canvas.create_rectangle(
                    x1, y1, x2, y2, fill=BLUE_COLOR, outline=RED_COLOR
                ),
            )
        window.update()

# ------------------------------------------------------------------
# Logical Functions:
# The modules required to carry out game logic
# ------------------------------------------------------------------
def update_snake(key):
    # Check if it hit the wall or its own body
    tail = snake[0]
    head = snake[-1]
    if tail != old_apple_cell:
        snake.pop(0)
    if key == "Left":
        snake.append((head[0] - 1, head[1]))
    elif key == "Right":
        snake.append((head[0] + 1, head[1]))
    elif key == "Up":
        snake.append((head[0], head[1] - 1))
    elif key == "Down":
        snake.append((head[0], head[1] + 1))

    head = snake[-1]
    if (
            head[0] > cols - 1
            or head[0] < 0
            or head[1] > rows - 1
            or head[1] < 0
            or len(set(snake)) != len(snake)
    ):
        # Hit the wall / Hit on body
        crashed = True
    elif apple_cell == head:
        # Got the apple
        old_apple_cell = apple_cell
        canvas.delete(apple_obj)
        place_apple()
        display_snake()
    else:
        snake_heading = key
        display_snake()

def check_if_key_valid( key):
    valid_keys = ["Up", "Down", "Left", "Right"]
    if key in valid_keys and forbidden_actions[snake_heading] != key:
        return True
    else:
        return False

def mouse_input(event):
    play_again()

def key_input(event):
    if not crashed:
        key_pressed = event.keysym
        # Check if the pressed key is a valid key
        if check_if_key_valid(key_pressed):
            # print(key_pressed)
            begin = True
            last_key = key_pressed



window = Tk()
window.title("Snake-and-Apple")
canvas = Canvas(window, width=size_of_board, height=size_of_board)
canvas.pack()
# Input from user in form of clicks and keyboard
window.bind("<Key>", key_input)
window.bind("<Button-1>", mouse_input)
play_again()
begin = False
