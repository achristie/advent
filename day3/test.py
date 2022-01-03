def main():
    gamma, epsilon = part1()

    print("part 1 -------------")
    print("gamma:", gamma)
    print("epsilon:", epsilon)
    print("decimal gamma:", int(gamma, 2))
    print("decimal epsilon:", int(epsilon, 2))
    print("product:", int(gamma, 2) * int(epsilon, 2))

    print("part 2 -------------")
    part2(gamma, epsilon)
    # print(filter_list(["110001010111", "101111011110"], 1, "1"))


def part2(gamma, epsilon):
    lst = []
    print(gamma)
    with open("input.txt") as file:
        for line in file:
            lst.append(line.rstrip())

    oxy = lst[:]
    co2 = lst[:]

    for i in range(12):
        oxygen_generator_rtg = filter_list(oxy, i, str(gamma[i]))
        # co2_scrubber_rtg = filter_list(co2, i, epsilon[i])

    print(oxygen_generator_rtg)
    # print(co2_scrubber_rtg)


def filter_list(lst, idx, value):
    new_lst = []
    for l in lst:
        if l[idx] == value:
            new_lst.append(l)

    # if len(new_lst) == 0:
    #     return lst[::-1]
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

    return (gamma, epsilon)


if __name__ == "__main__":
    main()
