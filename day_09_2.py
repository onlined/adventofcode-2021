import sys
from collections import deque

rows = sys.stdin.read().strip().split('\n')
rows = [list(map(int, row.strip())) for row in rows]


def is_low_point(rows, i, j):
    if i > 0 and rows[i-1][j] <= rows[i][j]:
        return False
    if i < len(rows) - 1 and rows[i+1][j] <= rows[i][j]:
        return False
    if j > 0 and rows[i][j-1] <= rows[i][j]:
        return False
    if j < len(rows[i]) - 1 and rows[i][j+1] <= rows[i][j]:
        return False
    return True


def get_basin_size(rows, i, j):
    visited = set()
    q = deque([(i, j)])
    while q:
        i, j = q.pop()
        if i < 0 or i > len(rows) - 1:
            continue
        if j < 0 or j > len(rows[i]) - 1:
            continue
        if rows[i][j] == 9:
            continue
        if (i, j) in visited:
            continue

        visited.add((i, j))

        q.extendleft([(i+1, j), (i-1, j), (i, j+1), (i, j-1)])

    return len(visited)


basin_sizes = []
for i in range(len(rows)):
    for j in range(len(rows[i])):
        if is_low_point(rows, i, j):
            basin_sizes.append(get_basin_size(rows, i, j))

basin_sizes.sort()

print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])
