import sys

nums = list(map(int, sys.stdin.read().split(',')))

possible = range(min(nums), max(nums) + 1)


print(min(sum(abs(x-n) for x in nums) for n in possible))

