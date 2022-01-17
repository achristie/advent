grid = [[int(i) for i in d] for d in open("input.txt").read().splitlines()]
x_size = len(grid)
y_size = len(grid[0])


def find_adj(point):
    points = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, -1), (-1, 1), (1, 1), (-1, -1)]
    adj = []
    for p in points:
        x = point[0] + p[0]
        y = point[1] + p[1]
        if x >= 0 and x < x_size and y >= 0 and y < y_size:
            adj.append((x, y))
    return adj


def flash(point, grid):
    adj = find_adj(point)
    for p in adj:
        grid[p[0]][p[1]] += 1
    return grid


def reset_flashed(flashed, grid):
    for f in flashed:
        grid[f[0]][f[1]] = 0
    return grid


def run_step(grid):
    grid = [[x + 1 for x in y] for y in grid]
    flashed = []

    def check_flash(grid):
        flag = False
        for x, v in enumerate(grid):
            for y, v2 in enumerate(v):
                if v2 > 9 and (x, y) not in flashed:
                    flag = True
                    grid = flash((x, y), grid)
                    flashed.append((x, y))
        if flag:
            return check_flash(grid)
        return grid

    check_flash(grid)
    reset_flashed(flashed, grid)
    return len(flashed), grid


running_total = 0
for i in range(100):
    count, grid = run_step(grid)
    running_total += count
    print(running_total)
