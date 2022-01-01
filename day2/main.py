class Sub:
    def __init__(self, depth, position, aim):
        self.depth = depth
        self.position = position
        self.aim = aim

    def dive(self, depth=0):
        self.depth += depth

    def forward(self, position=0):
        self.position += position

    def move(self, value=0):
        self.position += value
        self.depth += value * self.aim

    def adjust_aim(self, value=0):
        self.aim += value


def main():
    s = Sub(0, 0, 0)
    s2 = Sub(0, 0, 0)
    with open("input.txt") as file:
        for line in file:
            line = line.rstrip().split(" ")
            dir = line[0]
            mag = int(line[1])
            if dir == "up":
                s.dive(-mag)
                s2.adjust_aim(-mag)
            elif dir == "down":
                s.dive(mag)
                s2.adjust_aim(mag)
            elif dir == "forward":
                s.forward(mag)
                s2.move(mag)
            else:
                print("undefined direction: ", dir)

    print("Sub1------------")
    print("Depth:", s.depth)
    print("Position:", s.position)
    print("Multiplied:", s.position * s.depth)

    print("Sub2------------")
    print("Depth:", s2.depth)
    print("Position:", s2.position)
    print("Multiplied:", s2.position * s2.depth)


if __name__ == "__main__":
    main()
