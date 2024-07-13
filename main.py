from pallette import pallette
from turtle import Turtle, Screen
import random

hirst = Turtle()
hirst.hideturtle()
screen = Screen()
screen.colormode(255)


def print_row_of_dots(num_dots, dot_size):
    for n in range(num_dots):
        dot_color = random.choice(pallette)
        hirst.dot(dot_size, dot_color)
        hirst.penup()
        hirst.forward(50)


def create_spot_painting(num_rows, num_cols):
    row_spacing, spot_size = 30, 20
    hirst.speed(0)
    hirst.penup()
    hirst.goto(-250, -250)
    hirst.pendown()
    current_pos = hirst.position()
    for _ in range(num_rows):
        print_row_of_dots(num_cols, spot_size)
        y_shift = current_pos[1] + spot_size + row_spacing
        current_pos = (current_pos[0], y_shift)
        hirst.goto(current_pos)


create_spot_painting(10, 10)
screen.exitonclick()
