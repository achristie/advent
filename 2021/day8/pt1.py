data = [d.split(" | ")[1] for d in open("input.txt").read().splitlines()]
outputs = [item for d in data for item in d.split(" ")]

# 1 has 2 char, #4 has 4 char, #7 has 3 char, #8 has 7 char
def is_1478(output):
    length = len(output)
    return length == 2 or length == 3 or length == 4 or length == 7


print(sum(1 for o in outputs if is_1478(o)))
