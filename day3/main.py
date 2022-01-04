def main():
    gamma, epsilon = part1()

    print("part 1 -------------")
    print("gamma:", gamma)
    print("epsilon:", epsilon)
    print("decimal gamma:", int(gamma, 2))
    print("decimal epsilon:", int(epsilon, 2))
    print("product:", int(gamma, 2) * int(epsilon, 2))

    oxy, co2 = part2()
    print("part 2 -------------")
    print("oxy:", oxy)
    print("co2:", co2)
    print("decimal oxy:", int(oxy, 2))
    print("decimal co2:", int(co2, 2))
    print("life support:", int(oxy, 2) * int(co2, 2))

    print(not most_common_digit(["1100010110", "1100110100"], 5))


def part2():
    lst = []
    with open("input.txt") as file:
        for line in file:
            lst.append(line.rstrip())

    oxy = lst[:]
    co2 = lst[:]

    for i in range(12):
        oxy = filter_list(oxy, i, most_common_digit(oxy, i))
        co2 = filter_list(co2, i, not most_common_digit(co2, i))

    return oxy[0], co2[0]


def most_common_digit(lst, idx):
    length = len(lst)
    relevant_digit = map(lambda x: int(x[idx]), lst)
    return True if sum(relevant_digit) >= length / 2 else False


def filter_list(lst, idx, value):
    new_lst = []
    for l in lst:
        if int(l[idx]) == int(value):
            new_lst.append(l)

    if len(new_lst) == 0:
        return lst[::-1]
    return new_lst


def part1():
    lst = list(range(12))
    length = 0
    with open("input.txt") as file:
        for line in file:
            length += 1
            for i, s in enumerate(line.rstrip()):
                lst[i] += int(s)
    gamma = "".join(["1" if (num > length / 2) else "0" for num in lst])
    epsilon = "".join(["1" if (num <= length / 2) else "0" for num in lst])

    return gamma, epsilon


if __name__ == "__main__":
    main()
