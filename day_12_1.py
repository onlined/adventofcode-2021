import sys
from collections import defaultdict, deque

edges = map(str.strip, sys.stdin.read().strip().split('\n'))

graph = defaultdict(set)
for edge in edges:
    v1, v2 = edge.split('-')
    graph[v1].add(v2)
    graph[v2].add(v1)

paths = 0
q = deque([([], "start")])
while q:
    path, v = q.pop()
    if v == "end":
        paths += 1
        continue
    if v.islower() and v in path:
        continue
    for neighbor in graph[v]:
        q.appendleft((path + [v], neighbor))

print(paths)
