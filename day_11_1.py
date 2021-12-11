import sys
from collections import deque

rows = sys.stdin.read().strip().split('\n')
rows = [list(map(int, row.strip())) for row in rows]


def visit(rows, i, j, flashed):
    n = 0
    q = deque([(i,j)])
    while q:
        i, j = q.pop()
        if i < 0 or i > len(rows) - 1:
            continue
        if j < 0 or j > len(rows[i]) - 1:
            continue
        if (i, j) in flashed:
            continue

        if rows[i][j] == 9:
            rows[i][j] = 0
            flashed.add((i, j))
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    if x == i and y == j:
                        continue
                    q.appendleft((x, y))
        else:
            rows[i][j] += 1


flash_count = 0
for i in range(100):
    flashed = set()
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            visit(rows, i, j, flashed)

    flash_count += len(flashed)

print(flash_count)


