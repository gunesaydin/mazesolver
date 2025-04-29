import random

from cell import Cell
from line import Line
from point import Point
from window import Window

def main():
    win = Window(800, 600)

    cells = seed_random_cells(10, win)
    for cell in cells:
        cell.draw()

    for i in range(1, len(cells)):
        if random.choice([True, False]):
            cells[i-1].draw_move(cells[i])

    win.wait_for_close()

def seed_random_cells(num_of_cells:int, win:Window) -> list[Cell]:
    cells = []
    for i in range(num_of_cells):
        p1 = Point(i * 30 + 10, 10)
        p2 = Point(i * 30 + 30, 30)
        has_left_wall = random.choice([True, False])
        has_top_wall = random.choice([True, False])
        has_right_wall = random.choice([True, False])
        has_bottom_wall = random.choice([True, False])
        new_line = Cell(win, p1, p2, has_left_wall, has_top_wall, has_right_wall, has_bottom_wall)
        cells.append(new_line)

    return cells


main()