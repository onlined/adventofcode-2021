import sys

nums = list(map(int, sys.stdin.read().split(',')))

sums = []
for n in range(min(nums), max(nums) + 1):
    s = 0
    for x in nums:
        d = abs(x-n)
        s += d*(d+1)//2
    sums.append(s)

print(min(sums))

