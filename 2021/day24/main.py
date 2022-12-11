instructions = [d.split(" ") for d in open("input_test.txt").read().splitlines()]

variables = {"w": 0, "x": 0, "y": 0, "z": 0}


def inject_val(var2):
    return int(var2) if var2 not in ["w", "x", "y", "z"] else variables[var2]


def add(var1, var2):
    a = variables[var1]
    b = inject_val(var2)
    return a + b


def inp(var1):
    return variables[var1]


def div(a, b):
    a = variables[a]
    b = inject_val(b)
    return a // b


def mod(a, b):
    a = variables[a]
    b = inject_val(b)
    return a % b


def mul(a, b):
    a = variables[a]
    b = inject_val(b)
    return a * b


def eql(a, b):
    a = variables[a]
    b = inject_val(b)

    return 0 if a == b else 1


def alu(model, instructions):
    model = str(model)
    count = 0
    for ins in instructions:
        f, *ab = ins

        if f == "inp":
            variables[ab[0]] = int(model[count])
            count += 1
        elif f == "add":
            variables[ab[0]] = add(ab[0], ab[1])
        elif f == "mod":
            variables[ab[0]] = mod(ab[0], ab[1])
        elif f == "div":
            variables[ab[0]] = div(ab[0], ab[1])

    return variables


for i in range(99999999999999, 99999999111111, -1):
    if "0" in str(i):
        continue
    v = alu(i, instructions)
    if v["z"] == 0:
        print("Model: ", i, v)
        break
    else:
        variables = {"w": 0, "x": 0, "y": 0, "z": 0}
