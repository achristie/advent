alg, img = open("input_test.txt").read().split("\n\n")
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


def add_dim(img):
    temp = img.copy()
    for x in temp:
        x.insert(0, ".")
        x.insert(len(x) + 1, ".")

    temp.insert(0, ["." for _ in range(len(x))])
    temp.insert(len(x), ["." for _ in range(len(x))])
    return temp


def optimize(img, alg, cycles):
    new_img = add_dim(img)
    temp_img = img.copy()
    for i in range(len(img)):
        for j in range(len(img[0])):
            lookup = bin((i, j), new_img)
            temp_img[i][j] = alg[lookup]

    return temp_img


# print(bin((3, 3), add_dim(img)))
# print(bin((3, 3), add_dim(img)))
# print(bin((3, 3), add_dim(img)))
# display_grid(optimize(img, alg, 1))

# display_grid(img)
# display_grid(add_dim(img))
# display_grid(img)
display_grid(add_dim(img))
display_grid(add_dim(img))
display_grid(img)
