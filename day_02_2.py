import sys

lines = sys.stdin.read().strip().split('\n')
tuples = [(d, int(n)) for d, n in (l.split(' ') for l in lines)]

depth = 0
horizontal_position = 0
aim = 0

for direction, n in tuples:
    if direction == "forward":
        horizontal_position += n
        depth += n * aim
    elif direction == "up":
        aim -= n
    elif direction == "down":
        aim += n

print(depth * horizontal_position)
