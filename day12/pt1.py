from collections import defaultdict
from pprint import pp

path_data = [p for p in open("input.txt").read().splitlines()]
graph = defaultdict(list)

for p in path_data:
    s, e = p.split("-")

    graph[s].append(e)
    if e != "end" and s != "start":
        graph[e].append(s)

pp(graph)


# def find_all_paths(graph, start, end):
#     def find_path(start, end, state):
#         if start.islower() and len(start) == 1:
#             state.append(start)
#         paths = []
#         for e in graph[start]:
#             if e == "end":
#                 paths.append(state)
#             elif e not in state:
#                 paths.append(find_path(e, end, state))
#         return paths
#         # if e.islower() and len(e) == 1 and e in state:

#         #     deadends.append(state)
#         #     return

#         # state = state.append(e)
#         # if e == end:
#         #     paths.append(state)
#         #     return
#         # else:
#         #     return find_path(e, end, state)

#     return find_path(start, end, [start])


def find_all_paths(graph, start, end, path=[]):
    paths = []
    new_path = path + [start]
    if start == end:
        return [new_path]
    for e in graph[start]:
        if e != "start" and e not in path or e.isupper():
            paths.extend(find_all_paths(graph, e, end, new_path))
    return paths


paths = find_all_paths(graph, "start", "end")
pp(paths)
print("Number of paths:", len(paths))
