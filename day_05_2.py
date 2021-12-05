import sys
from collections import defaultdict

lines = sys.stdin.read().strip().split('\n')

def point_csv_to_tuple(csv):
    a, b = csv.split(',')
    return (int(a), int(b))

segments = [tuple(point_csv_to_tuple(p) for p in l.split(' -> ')) for l in lines]

visited = defaultdict(int)

for (x1, y1), (x2, y2) in segments:
    if x1 == x2:
        min_y, max_y = sorted((y1, y2))
        for y in range(min_y, max_y+1):
            visited[(x1, y)] += 1
    elif y1 == y2:
        min_x, max_x = sorted((x1, x2))
        for x in range(min_x, max_x+1):
            visited[(x, y1)] += 1
    elif abs(x1 - x2) == abs(y1 - y2):
        x_dir = -1 if x1 > x2 else 1
        y_dir = -1 if y1 > y2 else 1
        for i in range(0, abs(x1 - x2) + 1):
            x = x1 + x_dir * i
            y = y1 + y_dir * i
            visited[(x, y)] += 1

multiple = 0
for count in visited.values():
    if count > 1:
        multiple += 1

print(multiple)


