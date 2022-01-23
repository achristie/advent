from string import hexdigits


data = [format(int(h, 16), "040b") for h in open("input_test.txt").read().splitlines()]
print(data)


for h in data[2:3]:
    h = h.lstrip("0")
    version = h[:3]
    type_id = h[3:6]
    num = ""

    if type_id == "100":
        for x in range(6, len(h), 5):
            cont, b = h[x], h[x + 1 : x + 5]
            if len(b) == 4:
                num += h[x + 1 : x + 5]
    else:
        length_type_id = h[6]

        if length_type_id == 0:


    print(int(num, 2))
