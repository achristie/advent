from pprint import pp
import numpy as np

data = [d for d in open("input.txt").read().split("\n\n")]


def tuplize(str):
    lst = str.split(",")
    return (int(lst[0]), int(lst[1]))


points = [tuplize(p) for p in data[0].split("\n")]


def fold_to_point(str):
    lst = str.split("=")
    if lst[0] == "x":
        return (int(lst[1]), 0)
    else:
        return (0, int(lst[1]))


folds = [fold_to_point(f.replace("fold along ", "")) for f in data[1].split("\n")]

max_x = max(p[0] for p in points) + 1
# max_y = max(p[1] for p in points) + 1
max_y = 895


grid = [[0 for x in range(max_x)] for y in range(max_y)]


def add_point_to_grid(grid, point):
    grid[point[1]][point[0]] = 1
    return grid


def fold_grid(grid, instruction):
    x = instruction[0]
    y = instruction[1]
    if y > 0:
        above_fold = grid[:y]
        below_fold = grid[y + 1 :]
        below_fold = below_fold[::-1]
        return np.array(above_fold) + np.array(below_fold)
    else:
        left_of_fold = [g[:x] for g in grid]
        right_of_fold = [g[x + 1 :] for g in grid]
        right_of_fold = np.fliplr(right_of_fold)
        return np.array(left_of_fold) + right_of_fold


def display_grid(grid):
    grid = np.where(grid == 0, ".", "#")
    for line in grid:
        print("".join(line))


for p in points:
    grid = add_point_to_grid(grid, p)

for f in folds:
    grid = fold_grid(grid, f)


display_grid(grid)
pp((grid > 0).sum())
