import sys

lines = sys.stdin.read().strip().split('\n')

count = 0

for line in lines:
    displayed_digits = line.split(' | ')[1].split(' ')
    count += len([d for d in displayed_digits if len(d) in [2, 3, 4, 7]])

print(count)

