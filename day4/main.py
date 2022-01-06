import numpy as np
from pprint import pprint


def main():
    lines = [line for line in open("input.txt").read().splitlines() if line != ""]
    numbers = lines[0]
    boards = lines[1:]
    boards_lst = []

    for i in boards:
        new_lst = i.split(" ")
        new_lst = [int(x) for x in new_lst if x]
        boards_lst.append(new_lst)

    lst = [boards_lst[i : i + 5] for i in range(0, len(boards_lst), 5)]

    pprint(np.array(lst)[0])


if __name__ == "__main__":
    main()
