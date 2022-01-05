import numpy as np


def main():
    lines = [line for line in open("input.txt").read().splitlines() if line != ""]
    numbers = lines[0]
    boards = lines[1:]
    # print(numbers)
    # print(boards)
    lst = [boards[i : i + 5] for i in range(0, len(boards), 5)]
    print(lst[0], lst[1])
    # print(list(zip(*lst[0])))
    # print(lst[0][0].split())

    print(list(map(lambda x: x.split(), lst)))


if __name__ == "__main__":
    main()
