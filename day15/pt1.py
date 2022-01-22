from pprint import pp
from time import time
import heapq

grid = [[int(x) for x in l] for l in open("input_test.txt").read().splitlines()]
x_size = len(grid)
y_size = len(grid[0])


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        print(f"\nTime required: {(time() - start_time)*1000:.2f} ms")
        return result

    return wrapper


def find_adj(point):
    x, y = point[0], point[1]
    lst = []
    adj = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for ax, ay in adj:
        xi = x + ax
        yi = y + ay
        if x_size > xi >= 0 <= yi < y_size:
            lst.append((xi, yi))
    return lst


def find_path(grid):
    visited = [[0] * len(r) for r in grid]
    paths = [(0, 0, 0)]  # total, y, x
    pa = [(0, 0, 0)]

    while True:
        total, x, y = heapq.heappop(paths)  # Get coordinates for lowest path
        print("hit")
        if (x, y) == (x_size - 1, y_size - 1):
            return total
        if visited[x][y]:
            continue
        visited[x][y] = 1
        for px, py in find_adj((x, y)):
            print(paths[0])
            if visited[x][y]:
                continue
            heapq.heappush(paths, (total + grid[px][py], px, py))


print(find_path(grid))


@timer
def shortest_path(grid):
    y_size, x_size = len(grid), len(grid[0])
    paths = [(0, 0, 0)]  # total, y, x
    visited = [[0] * len(row) for row in grid]
    while True:
        total, y, x = heapq.heappop(paths)  # Get coordinates for lowest path
        if visited[y][x]:
            continue
        if (y, x) == (y_size - 1, x_size - 1):
            return total
        visited[y][x] = 1
        for ny, nx in [
            (y + 1, x),
            (y, x + 1),
            (y - 1, x),
            (y, x - 1),
        ]:  # prefer down and right
            if not x_size > ny >= 0 <= nx < y_size:
                continue
            if visited[ny][nx]:
                continue
            # print(ny, nx)
            heapq.heappush(paths, (total + grid[ny][nx], ny, nx))


print(shortest_path(grid))
