from tkinter import Canvas

from point import Point

class Line():
    def __init__(self, p1:Point, p2:Point):
        self.__p1 = p1
        self.__p2 = p2

    def draw(self, canvas:Canvas, fill_color:str):
        canvas.create_line()