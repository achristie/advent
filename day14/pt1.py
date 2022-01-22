from collections import Counter

data = [d for d in open("input_test.txt").read().splitlines()]
template = data[0]
rules = data[2:]

rules = {p.split(" -> ")[0]: p.split(" -> ")[1] for p in rules}

print(template, rules)


def get_template_pairs(template):
    return [
        template[i] + template[i + 1] for i, _ in enumerate(range(len(template) - 1))
    ]


def execute(template, rules, steps=2):
    for i in range(steps):
        pairs = get_template_pairs(template)
        template = execute_step(pairs, rules)
    return template


def execute_step(template_pairs, rules):
    lst = []
    flag = True

    for tp in template_pairs:
        if flag:
            new_tp = tp[0] + rules[tp] + tp[1]
            flag = False
        else:
            new_tp = rules[tp] + tp[1]
        lst.append(new_tp)
    return "".join(lst)


execution = execute(template, rules, steps=10)
c = Counter(execution)
print(c)
print("Most Common:", c.most_common(1))
print("Least Common:", c.most_common()[:-2:-1])
print("Difference:", c.most_common(1)[0][1] - c.most_common()[:-2:-1][0][1])
