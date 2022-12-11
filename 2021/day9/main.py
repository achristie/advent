from collections import namedtuple, Counter, defaultdict
from pprint import pp

data = [
    [int("".join(i.split())) for i in d] for d in open("input.txt").read().splitlines()
]
Point = namedtuple("Point", "x y")
x_size = len(data)
y_size = len(data[0])


def find_lowpoints(data):
    lst = []
    for i, e in enumerate(data):
        for j, n in enumerate(e):
            below, above, right, left = 10, 10, 10, 10
            if i > 0:
                above = data[i - 1][j]
            if j > 0:
                left = data[i][j - 1]
            if j < len(e) - 1:
                right = data[i][j + 1]
            if i < len(data) - 1:
                below = data[i + 1][j]

            if n < below and n < above and n < right and n < left:
                lst.append((n, Point(i, j)))

    return lst


def find_adj(point):
    adj = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    points = []

    for dx, dy in adj:
        if (
            point.x + dx >= 0
            and point.x + dx < x_size
            and point.y + dy >= 0
            and point.y + dy < y_size
        ):
            points.append(Point(point.x + dx, point.y + dy))

    return points


def find_basins(lowpoints):
    basins = defaultdict(set)

    def find_basin(point, lp):
        for p in find_adj(point):
            if data[p.x][p.y] > data[point.x][point.y] and data[p.x][p.y] < 9:
                basins[lp].add(p)
                find_basin(p, lp)

    for lp in lowpoints:
        find_basin(lp[1], lp[1])

    return basins


lowpoints = find_lowpoints(data)
print("Low points:", lowpoints)
print("Risk:", sum(x[0] + 1 for x in find_lowpoints(data)))
basins = find_basins(lowpoints)
print("Basins:")
pp({k: len(v) + 1 for k, v in sorted(basins.items(), key=lambda x: len(x[1]))})
