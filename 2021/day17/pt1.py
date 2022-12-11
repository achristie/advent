from os import write


target = open("input.txt").read().removeprefix("target area: ").split(",")
x, y = [t.split("=")[1].split("..") for t in target]
x = (int(x[0]), int(x[1]))
y = (int(y[0]), int(y[1]))

print(x, y)


def execute_step(velo, position):
    x, y = position
    dx, dy = velo
    x += dx
    y += dy

    if dx != 0:
        dx += 1 if dx < 0 else -1

    dy -= 1

    return (x, y), (dx, dy)


def within_area(area, position):
    x_min, x_max = area[0][0], area[0][1]
    y_min, y_max = area[1][0], area[1][1]
    x, y = position

    return x_min <= x <= x_max and y_min <= y <= y_max


def beyond_area(area, position):
    x_min, x_max = area[0][0], area[0][1]
    y_min, y_max = area[1][0], area[1][1]
    x, y = position

    return x > x_max or y < y_min


def simulate(area):
    pos = (0, 0)
    intercepts = []  # height, dx, dy
    for i in range(400):
        for j in range(-500, 500):
            pos = (0, 0)
            y_prime = 0
            vi = (i, j)
            v = (i, j)
            counts = False
            while True:
                pos, v = execute_step(v, pos)
                y_prime = y_prime if pos[1] <= y_prime else pos[1]
                if within_area(area, pos):
                    counts = True

                if beyond_area(area, pos):
                    break

            if counts:
                intercepts.append((y_prime, vi[0], vi[1]))

    return intercepts


intercepts = simulate((x, y))
print("Largest Intercept", sorted(intercepts, key=lambda x: x[0], reverse=True)[0])
print("Count of intercepts", len(intercepts))
