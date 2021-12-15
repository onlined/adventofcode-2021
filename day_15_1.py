import sys
from collections import deque
import copy

lines = map(str.strip, sys.stdin.read().strip().split('\n'))
cavern = [list(map(int, list(l))) for l in lines]

q = deque([((0, 0), 0, set())])
min_risks = copy.deepcopy(cavern)
for row in min_risks:
    for j in range(len(row)):
        row[j] = float('inf')

while q:
    (i, j), risk, visited = q.pop()
    if (i, j) in visited:
        continue

    if (i, j) == (len(cavern) - 1, len(cavern[-1]) - 1):
        if risk < min_risks[-1][-1]:
            min_risks[-1][-1] = risk
        continue

    if risk >= min_risks[i][j]:
        continue
    min_risks[i][j] = risk
    visited = visited | {(i, j)}

    if i < len(cavern) - 1:
        q.appendleft(((i+1, j), risk + cavern[i+1][j], visited))
    if j < len(cavern[i]) - 1:
        q.appendleft(((i, j+1), risk + cavern[i][j+1], visited))
    if i > 0:
       q.appendleft(((i-1, j), risk + cavern[i-1][j], visited))
    if j > 0:
       q.appendleft(((i, j-1), risk + cavern[i][j-1], visited))


print(min_risks[-1][-1])

