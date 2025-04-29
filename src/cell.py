from line import Line
from point import Point
from window import Window

class Cell():
    def __init__(
        self, win:Window, p1:Point, p2:Point, has_left_wall=True, has_top_wall=True, has_right_wall=True, has_bottom_wall=True
    ):
        self.__win = win
        self.p1 = p1
        self.p2 = p2
        self.__has_left_wall = has_left_wall
        self.__has_top_wall = has_top_wall
        self.__has_right_wall = has_right_wall
        self.__has_bottom_wall = has_bottom_wall

    def draw(self):
        if self.__has_left_wall:
            left_wall_line = Line(self.p1, Point(self.p1.x, self.p2.y))
            self.__win.draw_line(left_wall_line)

        if self.__has_top_wall:
            top_wall_line = Line(self.p1, Point(self.p2.x, self.p1.y))
            self.__win.draw_line(top_wall_line)

        if self.__has_right_wall:
            right_wall_line = Line(Point(self.p2.x, self.p1.y), self.p2)
            self.__win.draw_line(right_wall_line)

        if self.__has_bottom_wall:
            bottom_wall_line = Line(Point(self.p1.x, self.p2.y), self.p2)
            self.__win.draw_line(bottom_wall_line)

    def draw_move(self, to_cell, undo=False):
        self_center = Point((self.p1.x + self.p2.x) / 2, (self.p1.y + self.p2.y) / 2)
        target_center = Point((to_cell.p1.x + to_cell.p2.x) / 2, (to_cell.p1.y + to_cell.p2.y) / 2)
        move_line = Line(self_center, target_center)
        if undo:
            self.__win.draw_line(move_line, "grey")
        else:
            self.__win.draw_line(move_line, "red")