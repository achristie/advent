lines = [l for l in open("input_test.txt").read().splitlines()]
tags = {"[": "]", "(": ")", "<": ">", "{": "}"}
points = {")": 1, "]": 2, "}": 3, ">": 4}


def find_opens(line):
    state = []
    for s in line:
        if s in tags:
            state.append(s)
        elif tags[state[-1]] == s:
            state.pop()
        else:
            return "corrupt"
    return state


for l in lines:
    results = find_opens(l)
    if results != corrupt:
      out
