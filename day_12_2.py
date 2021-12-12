import sys
from collections import Counter, defaultdict, deque

edges = map(str.strip, sys.stdin.read().strip().split('\n'))

graph = defaultdict(set)
for edge in edges:
    v1, v2 = edge.split('-')
    if v1 != "end" and v2 != "start":
        graph[v1].add(v2)
    if v1 != "start" and v2 != "end":
        graph[v2].add(v1)

paths = 0
q = deque([["start"]])
while q:
    path = q.pop()
    small_caves = [cave for cave in path if cave.islower()]
    if len(small_caves) - len(set(small_caves)) > 1:
        continue
    v = path[-1]
    if v == "end":
        paths += 1
        continue
    for neighbor in graph[v]:
       q.appendleft((path + [neighbor]))

print(paths)
