def main():
    fish = [int(fish) for fish in open("input.txt").read().split(",")]
    counts = {}

    for i in range(9):
        counts[i] = fish.count(i)

    print(counts)

    for i in range(256):
        new_fish = counts[0]
        for i in range(8):
            counts[i] = counts[i + 1]
        counts[8] = new_fish
        counts[6] += new_fish

    print(counts)
    print(f"Sum: {sum(counts.values())}")


if __name__ == "__main__":
    main()
