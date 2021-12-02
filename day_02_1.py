import sys

lines = sys.stdin.read().strip().split('\n')
tuples = [(d, int(n)) for d, n in (l.split(' ') for l in lines)]

depth = 0
horizontal_position = 0

for direction, distance in tuples:
    if direction == "forward":
        horizontal_position += distance
    elif direction == "up":
        depth -= distance
    elif direction == "down":
        depth += distance

print(depth * horizontal_position)
