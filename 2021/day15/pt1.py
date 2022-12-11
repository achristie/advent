from pprint import pp
from time import time
import heapq
import itertools

grid = [[int(x) for x in l] for l in open("input.txt").read().splitlines()]
x_size = len(grid)
y_size = len(grid[0])


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        print(f"\nTime required: {(time() - start_time)*1000:.2f} ms")
        return result

    return wrapper


def find_adj(point, x_size, y_size):
    x, y = point[0], point[1]
    lst = []
    adj = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for ax, ay in adj:
        xi = x + ax
        yi = y + ay
        if x_size > xi >= 0 <= yi < y_size:
            lst.append((xi, yi))
    return lst


def create_plusone_grid(grid):
    return [[(x - 1) % 9 + 1 for x in y] for y in grid]


def get_new_value(val, x_iter, y_iter):
    return ((val + x_iter + y_iter - 1) % 9) + 1


def make_large_grid(grid, size=(5, 5)):
    xs, ys = size
    new_grid = [[0] * len(i) * ys for i in grid * xs]
    for x in range(len(new_grid)):
        for y in range(len(new_grid[0])):
            new_grid[x][y] = get_new_value(
                grid[x % len(grid)][y % len(grid[0])],
                x // x_size,
                y // y_size,
            )
    return new_grid


@timer
def find_path(grid):
    visited = [[0] * len(r) for r in grid]
    pq = [(0, 0, 0)]
    y_size = len(grid)
    x_size = len(grid[0])

    while True:
        total, x, y = heapq.heappop(pq)
        if (x, y) == (x_size - 1, y_size - 1):
            return (total, x, y)
        if visited[x][y]:
            continue
        visited[x][y] = 1
        for px, py in find_adj((x, y), x_size, y_size):
            if visited[px][py]:
                continue
            heapq.heappush(pq, (total + grid[px][py], px, py))


print("Risk:", find_path(grid))

large_grid = make_large_grid(grid, size=(5, 5))
print(len(large_grid), len(large_grid[0]))

print("Large Grid Risk:", find_path(large_grid))
