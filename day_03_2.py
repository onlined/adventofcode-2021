import sys

nums = sys.stdin.read().strip().split('\n')
num_len = len(nums[0])


def get_zero_count(nums, digit):
    if not nums:
        return 0

    num_len = len(nums[0])
    zero_count = 0
    for num in nums:
        if num[digit] == "0":
            zero_count += 1

    return zero_count


tmp = nums[:]
for i in range(num_len):
    if len(tmp) == 1:
        break

    zero_count = get_zero_count(tmp, i)
    one_count = len(tmp) - zero_count
    keep_with_bit = "0" if zero_count > one_count else "1"
    tmp = [num for num in tmp if num[i] == keep_with_bit]

co2_scrubber_rating = int(tmp[0], 2)

tmp = nums[:]
for i in range(num_len):
    if len(tmp) == 1:
        break

    zero_count = get_zero_count(tmp, i)
    one_count = len(tmp) - zero_count
    keep_with_bit = "1" if zero_count > one_count else "0"
    tmp = [num for num in tmp if num[i] == keep_with_bit]

oxygen_generator_rating = int(tmp[0], 2)

print(co2_scrubber_rating * oxygen_generator_rating)
