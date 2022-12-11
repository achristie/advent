lines = [l for l in open("input.txt").read().splitlines()]
tags = {"[": "]", "(": ")", "<": ">", "{": "}"}
points = {"(": 1, "[": 2, "{": 3, "<": 4}


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


def get_scores(line):
    running_total = 0
    results = find_opens(l)
    if results != "corrupt":
        for s in results[::-1]:
            running_total = running_total * 5 + points[s]
    return running_total


scores = []
for l in lines:
    sc = get_scores(l)
    if sc > 0:
        scores.append(sc)

print(sorted(scores))
print("middle score:", sorted(scores)[len(scores) // 2])
