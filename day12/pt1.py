from collections import defaultdict
from pprint import pp
from functools import cache

path_data = [p for p in open("input_test.txt").read().splitlines()]
graph = defaultdict(list)

for p in path_data:
    s, e = p.split("-")

    graph[s].append(e)
    if e != "end" and s != "start":
        graph[e].append(s)

pp(graph)


def find_all_paths2(graph, start, end):
    paths = []

    @cache
    def find_path(start, end, state=()):
        new_state = state + (start,)
        print(new_state)
        if start == end:
            paths.append(new_state)
        for e in graph[start]:
            if e.isupper() or (e not in state and e != "start"):
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


# paths = find_all_paths(graph, "start", "end")
# pp(paths)
# print("Number of paths:", len(paths))

p2 = find_all_paths2(graph, "start", "end")
pp(p2)
