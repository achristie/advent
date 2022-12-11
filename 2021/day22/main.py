from itertools import product


def format_data(item):
    rule, cube = item.split(" ")
    d = {}
    cube = cube.split(",")
    for l in cube:
        var, point = l.split("=")
        point = [int(p) for p in point.split("..")]
        d[var] = (min(point), max(point))

    return (rule, d)


def bound_number(number):
    if number >= 0:
        return number if -50 <= number <= 50 else 50
    else:
        return number if -50 <= number <= 50 else -50


def get_cuboid(ranges):
    xs, xe = ranges["x"]
    ys, ye = ranges["y"]
    zs, ze = ranges["z"]

    for p in [xs, xe, ys, ye, zs, ze]:
        if p not in range(-50, 51):
            return False

    return product(range(xs, xe + 1), range(ys, ye + 1), range(zs, ze + 1), repeat=1)


def execute_step(step, state):
    rule, coords = step

    coords = get_cuboid(coords)
    if not coords:
        return state

    for c in coords:
        state[c] = rule

    return state


steps = [format_data(x) for x in open("input_test.txt").read().splitlines()]


state = {}
for s in steps:
    state = execute_step(s, state)


print("On: ", sum(1 for v in state.values() if v == "on"))
print("Off: ", sum(1 for v in state.values() if v == "off"))
# print(state)
