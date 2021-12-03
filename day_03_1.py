import sys

nums = sys.stdin.read().strip().split('\n')
num_len = len(nums[0])
zero_counts = [0 for _ in range(num_len)]

for num in nums:
    for i in range(num_len):
        if num[i] == "0":
            zero_counts[i] += 1

gamma_rate = []
epsilon_rate = []

for zero_count in zero_counts:
    one_count = len(nums) - zero_count
    assert zero_count != one_count

    gamma_rate.append("0" if zero_count > one_count else "1")
    epsilon_rate.append("1" if zero_count > one_count else "0")

gamma_rate = int("".join(gamma_rate), 2)
epsilon_rate = int("".join(epsilon_rate), 2)

print(gamma_rate * epsilon_rate)
