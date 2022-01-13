from pprint import pp

output = [d.split(" | ")[0] for d in open("input_test.txt").read().splitlines()]


def find_1478(input):
    length = len(input)
    s = set(input)
    if length == 2:
        return {"1": s}
    if length == 4:
        return {"4": s}
    if length == 3:
        return {"7": s}
    if length == 7:
        return {"8": s}
    return {}


def find_603(input, d):
    length = len(input)
    s = set(input)
    if length == 6 and not d["1"] <= s:
        return {"6": s}
    if length == 6 and not d["4"] <= s:
        return {"0": s}
    if length == 5 and d["1"] <= s:
        return {"3": s}
    return {}


def find_925(input, d):
    length = len(input)
    s = set(input)
    if length == 6 and s != d["6"] and s != d["0"]:
        return {"9": s}
    if length == 5 and len(s.intersection(d["6"])) == 4:
        return {"2": s}
    if length == 5 and len(s.intersection(d["6"])) == 5:
        return {"5": s}

    return {}


for o in output[:1]:
    d = {}
    for s in o.split(" "):
        d.update(find_1478(s))

    for s in o.split(" "):
        d.update(find_603(s, d))

    for s in o.split(" "):
        d.update(find_925(s, d))

    pp(d)
