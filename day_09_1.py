import sys

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


total = 0
for i in range(len(rows)):
    for j in range(len(rows[i])):
        if is_low_point(rows, i, j):
            total += 1 + rows[i][j]


print(total)
