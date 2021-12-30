def main():
    value = 0
    counter = 0
    skip = True
    with open("day1_input.txt") as file:
        for line in file:
            if skip:
                # skip the first entry
                skip = False
                continue
            else:
                nv = int(line.rstrip())
                if is_increase(value, nv):
                    counter += 1
                value = nv
    print(f"Count: {counter}")


def is_increase(initial_value, new_value):
    return new_value > initial_value


if __name__ == "__main__":
    main()
