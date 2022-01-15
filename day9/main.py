data = [
    [int("".join(i.split())) for i in d] for d in open("input.txt").read().splitlines()
]


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
                lst.append(n)

    return lst


lowpoints = find_lowpoints(data)
print("Low points:", lowpoints)
print("Risk:", sum(x + 1 for x in find_lowpoints(data)))
