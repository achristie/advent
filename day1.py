def main():
    col = get_collection(filename="day1_input.txt")
    print(sum(is_increase(rolling_sum(col=col, window=3))))
    print(sum(is_increase(col=col)))

    print(rolling_sum(window=1))


def get_collection(filename="day1_input.txt"):
    col = []
    with open(filename) as file:
        for line in file:
            col.append(int(line.rstrip()))

    return col


def is_increase(col=[1, 3, 4, 2]):
    new_col = []
    for i, val in enumerate(col[:-1]):
        new_col.append(1 if col[i] < col[i + 1] else 0)

    return new_col


def rolling_sum(col=[199, 200, 208, 210, 200, 207, 240, 269, 260, 263], window=3):
    lst = []
    for i, val in enumerate(col):
        if i < len(col) - window + 1:
            lst.append(sum(col[i : i + window]))
        else:
            break
    return lst


if __name__ == "__main__":
    main()
