from pprint import pprint
import numpy as np


def main():
    lines = [tuplize(line) for line in open("input.txt").read().splitlines()]
    only_straight = [
        line for line in lines if (line.is_horizontal() or line.is_vertical())
    ]

    grid = np.zeros((1000, 1000))
    for l in only_straight:
        grid += l.get_grid()

    pprint((grid >= 2).sum())
    pprint(grid)


class Line:
    def_grid = np.zeros((1000, 1000))

    def __init__(self, x1, x2, y1, y2):
        self.x1 = int(x1)
        self.x2 = int(x2)
        self.y1 = int(y1)
        self.y2 = int(y2)

    def __repr__(self):
        return f"({self.x1}, {self.y1}) -> ({self.x2}, {self.y2})"

    def __str__(self):
        return f"({self.x1}, {self.y1}) -> ({self.x2}, {self.y2})"

    def is_horizontal(self):
        return self.y1 == self.y2

    def is_vertical(self):
        return self.x1 == self.x2

    def get_grid(self):
        g = self.def_grid.copy()

        x_start = self.x1 if self.x1 < self.x2 else self.x2
        x_end = abs(self.x2 - self.x1)
        x_ones = np.ones(x_end + 1)

        y_start = self.y1 if self.y1 < self.y2 else self.y2
        y_end = abs(self.y2 - self.y1)
        y_ones = np.ones(y_end + 1)

        if self.is_horizontal():
            g[y_start, x_start : x_start + x_end + 1] = x_ones
        else:
            g[y_start : y_start + y_end + 1, x_start] = y_ones

        return g


def tuplize(line):
    one, two = line.split(" -> ")
    x1, y1 = one.split(",")
    x2, y2 = two.split(",")
    return Line(x1, x2, y1, y2)


if __name__ == "__main__":
    main()
