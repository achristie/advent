from pprint import pprint
import numpy as np

grid_size = (1000, 1000)


def main():
    lines = [tuplize(line) for line in open("input.txt").read().splitlines()]
    only_straight = [
        line for line in lines if (line.is_horizontal() or line.is_vertical())
    ]

    grid = np.zeros(grid_size, int)
    grid2 = np.zeros(grid_size, int)
    for l in only_straight:
        grid += l.get_grid()

    for l in lines:
        grid2 += l.get_grid()

    print("part 1:", (grid >= 2).sum())
    print("part 2:", (grid2 >= 2).sum())


class Line:
    def_grid = np.zeros(grid_size, int)

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

    def slope(self):
        return (self.y2 - self.y1) / (self.x2 - self.x1)

    def get_grid(self):
        g = self.def_grid.copy()

        x_start = self.x1 if self.x1 < self.x2 else self.x2
        x_len = abs(self.x2 - self.x1) + 1

        y_start = self.y1 if self.y1 < self.y2 else self.y2
        y_len = abs(self.y2 - self.y1) + 1

        if self.is_horizontal():
            x_ones = np.ones(x_len)
            g[y_start, x_start : x_start + x_len] = x_ones
        elif self.is_vertical():
            y_ones = np.ones(y_len)
            g[y_start : y_start + y_len, x_start] = y_ones
        else:
            mtx = np.zeros(x_len * y_len).reshape(x_len, y_len)
            if self.slope() > 0:
                np.fill_diagonal(mtx, 1)
            else:
                np.fill_diagonal(np.fliplr(mtx), 1)

            g[y_start : y_start + y_len, x_start : x_start + x_len] = mtx

        return g


def tuplize(line):
    one, two = line.split(" -> ")
    x1, y1 = one.split(",")
    x2, y2 = two.split(",")
    return Line(x1, x2, y1, y2)


if __name__ == "__main__":
    main()
