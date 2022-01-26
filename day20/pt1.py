import copy

alg, img = open("input.txt").read().split("\n\n")
img = [list(x) for x in img.splitlines()]


def get_adj(point):
    x, y = point
    adj = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
    lst = []
    for p in adj:
        px, py = p
        lst.append((x + px, y + py))

    return lst


def display_grid(img):
    for r in img:
        print("".join(r))


def bin(point, img):
    adj = get_adj(point)
    s = ""

    for p in adj:
        px, py = p
        try:
            temp = img[px][py]
            s += "0" if temp == "." else "1"
        except:
            s += "0"

    return int(s, 2)


def add_dim(img, alg, cycle):
    temp = copy.deepcopy(img)
    char = "#" if alg[0] == "#" and not cycle % 2 else "."
    for x in temp:
        x.insert(0, char)
        x.insert(len(x) + 1, char)

    temp.insert(0, ["." for _ in range(len(x))])
    temp.insert(len(x), ["." for _ in range(len(x))])
    return temp


def optimize(img, alg, cycles):
    def iterate(img, cycle):
        img = add_dim(img, alg, cycle)
        draft_img = copy.deepcopy(img)
        for i in range(len(img)):
            for j in range(len(img[0])):
                lookup = bin((i, j), img)
                draft_img[i][j] = alg[lookup]
        return draft_img

    for i in range(cycles):
        img = iterate(img, i)

    return img


output = optimize(img, alg, 2)
display_grid(output)
print("Count (2):", sum(x.count("#") for x in output))

output = optimize(img, alg, 50)
print("Count (50):", sum(x.count("#") for x in output))
