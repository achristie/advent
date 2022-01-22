from pprint import pp
from time import time
import heapq

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
    pq = [(0, 0, 0)]

    while True:
        total, x, y = heapq.heappop(pq)
        if (x, y) == (x_size - 1, y_size - 1):
            return (total, x, y)
        if visited[x][y]:
            continue
        visited[x][y] = 1
        for px, py in find_adj((x, y)):
            if visited[px][py]:
                continue
            heapq.heappush(pq, (total + grid[px][py], px, py))


print(find_path(grid))
