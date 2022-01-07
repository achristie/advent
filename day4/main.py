import itertools
import numpy as np
from pprint import pprint


def main():
    lines = [line for line in open("input.txt").read().splitlines() if line != ""]
    numbers = lines[0].split(",")
    boards = lines[1:]
    boards_lst = []

    for i in boards:
        new_lst = i.split(" ")
        new_lst = [int(x) for x in new_lst if x]
        boards_lst.append(new_lst)

    lst = [boards_lst[i : i + 5] for i in range(0, len(boards_lst), 5)]

    for n in numbers[:39]:
        lst = call_number(int(n), lst)
        winning_board = check_winner(lst)
        if winning_board:
            print("Winning board!")
            pprint(winning_board)
            print("sum:", np.sum(winning_board))
            print("number called:", n)
            print("product:", np.sum(winning_board) * int(n))
            break


def call_number(number, boards):
    print("Number is:", int(number))
    new_boards = []
    for b in boards:
        board = [[0 if number == j else j for j in i] for i in b]
        new_boards.append(board)
    return new_boards


def check_winner(boards):
    for b in boards:
        arr = np.array(b)
        if np.any(np.all(arr == 0, axis=0)) or np.any(np.all(arr == 0, axis=1)):
            return b


if __name__ == "__main__":
    main()
