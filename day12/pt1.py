from collections import defaultdict, Counter
from pprint import pp

path_data = [p for p in open("input.txt").read().splitlines()]
graph = defaultdict(list)

for p in path_data:
    s, e = p.split("-")

    graph[s].append(e)
    if e != "end" and s != "start":
        graph[e].append(s)

pp(graph)


def find_all_paths2(graph, start, end):
    paths = []

    def find_path(start, end, state=[]):
        new_state = state + [start]
        if start == end:
            paths.append(new_state)
        for e in graph[start]:
            if e != "start":
                if e.isupper():
                    find_path(e, end, new_state)
                else:
                    filtered = filter(lambda x: x.islower(), new_state)
                    c = Counter(filtered).most_common(1)
                    flag = True if c[0][1] > 1 else False

                    if (flag and new_state.count(e) < 1) or (
                        not flag and new_state.count(e) < 2
                    ):
                        find_path(e, end, new_state)

        return paths

    find_path(start, end)
    return paths


def find_all_paths(graph, start, end, path=[]):
    paths = []
    new_path = path + [start]
    if start == end:
        return [new_path]
    for e in graph[start]:
        if e != "start" and e not in path or e.isupper():
            paths.extend(find_all_paths(graph, e, end, new_path))
    return paths


p2 = find_all_paths2(graph, "start", "end")
# pp(p2)
p2 = [p for p in p2 if p.count("end") == 1]
pp(len(p2))
