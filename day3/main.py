def main():
    lst = list(range(12))
    length = 0
    with open("input.txt") as file:
        for line in file:
            length += 1
            for i, s in enumerate(line.rstrip()):
                lst[i] += int(s)
    gamma = "".join(["1" if (num > length / 2) else "0" for num in lst])
    epsilon = "".join(["1" if (num <= length / 2) else "0" for num in lst])
    print("length:", length)
    print("original list:", lst)
    print("gamma:", gamma)
    print("epsilon:", epsilon)
    print("decimal gamma:", int(gamma, 2))
    print("decimal epsilon:", int(epsilon, 2))
    print("product:", int(gamma, 2) * int(epsilon, 2))


if __name__ == "__main__":
    main()
