import sys

nums = list(map(int, sys.stdin.read().strip().split('\n')))

greater_count = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        greater_count += 1

print(greater_count)
