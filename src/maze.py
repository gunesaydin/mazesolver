import time

from cell import Cell
from point import Point
from window import Window

class Maze():
    def __init__(
        self,
        x1=int,
        y1=int,
        num_rows=int,
        num_cols=int,
        cell_size_x=int,
        cell_size_y=int,
        win=Window,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        self._cells = []

        self.__create_cells()

    def __create_cells(self):
        for i in range(self.__num_cols):
            self._cells.append([])
            for j in range(self.__num_rows):
                p1 = Point(self.__x1 + (self.__cell_size_x * i), self.__y1 + (self.__cell_size_y * j))
                p2 = Point(self.__x1 + (self.__cell_size_x * (i+1)), self.__y1 + (self.__cell_size_y * (j+1)))
                new_cell = Cell(self.__win, p1, p2)
                self._cells[i].append(new_cell)
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        self._cells[i][j].draw()
        self.__animate()

    def __animate(self):
        self.__win.redraw()
        time.sleep(0.01)