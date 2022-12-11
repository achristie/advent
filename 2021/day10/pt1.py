from collections import namedtuple

lines = [d for d in open("input.txt").read().splitlines()]
Tags = namedtuple("Tags", "open close")
pairs = [Tags("[", "]"), Tags("{", "}"), Tags("<", ">"), Tags("(", ")")]
points = {")": 3, "]": 57, "}": 1197, ">": 25137}


def replace_matching_tags(line):
    def replace(line):
        new_line = line
        for p in pairs:
            new_line = new_line.replace(p.open + p.close, "")

        if new_line != line:
            return replace(new_line)

        return line

    new_line = replace(line)
    return new_line


def find_first_mismatch(line):
    lowest_idx = len(line)
    for p in pairs:
        idx = line.find(p.close)
        if idx > 0 and idx < lowest_idx:
            lowest_idx = idx

    if lowest_idx > 0 and lowest_idx < len(line):
        return line[lowest_idx - 1 : lowest_idx + 1]

    return ""


def find_syntax_errors(line):
    lst = []
    for l in line:
        replaced = replace_matching_tags(l)
        mismatch = find_first_mismatch(replaced)
        if len(mismatch) > 0:
            print(
                replaced,
                f"Expected '{dict(pairs)[mismatch[0]]}', but found '{mismatch[1]}' instead",
            )
            lst.append(mismatch)

            # print("test")  # print(dict(pairs))
            # print(mismatch[0])
        # print(replaced)

    return lst


syntax_errors = find_syntax_errors(lines)
print("Points:", sum([points[s[1]] for s in syntax_errors]))
