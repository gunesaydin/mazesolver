from line import Line
from point import Point
from window import Window

def main():
    win = Window(800, 600)

    lines = seed_random_lines(10)
    for line in lines:
        win.draw_line(line, "red")

    win.wait_for_close()

def seed_random_lines(num_of_lines:int) -> list:
    lines = []
    for i in range(num_of_lines):
        p1 = Point(i * 10 + 10, 10)
        p2 = Point(i * 10 + 10, 110)
        new_line = Line(p1, p2)
        lines.append(new_line)

    return lines


main()