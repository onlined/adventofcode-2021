import sys
from functools import lru_cache


@lru_cache
def fish_count_from_single(fish, days):
    if fish > 0:
        days -= min(fish, days)

    if days == 0:
        return 1

    return fish_count_from_single(6, days - 1) + fish_count_from_single(8, days - 1)


def fish_count(initial, days):
    count = 0
    for fish in initial:
        count += fish_count_from_single(fish, days)
    return count


fish = list(map(int, sys.stdin.read().strip().split(',')))

print(fish_count(fish, 256))
