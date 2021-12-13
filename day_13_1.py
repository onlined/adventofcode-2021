import sys

lines = list(map(str.strip, sys.stdin.read().strip().split('\n')))

i = lines.index("")
points = set(tuple(map(int, l.split(','))) for l in lines[:i])
folds = [l.split(' ')[2].split('=') for l in lines[i+1:]]
folds = [(f[0], int(f[1])) for f in folds]

axis, val = folds[0]
new_points = set()
if axis == 'x':
    for x, y in points:
        if x > val:
            diff = x - val
            new_x = val - diff
            new_points.add((new_x, y))
        else:
            new_points.add((x, y))
elif axis == 'y':
    for x, y in points:
        if y > val:
            diff = y - val
            new_y = val - diff
            new_points.add((x, new_y))
        else:
            new_points.add((x, y))
else:
    assert False

points = new_points

print(len(points))
