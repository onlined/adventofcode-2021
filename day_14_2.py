import sys
from collections import Counter
from operator import itemgetter
from functools import lru_cache

polymer, _, *rules = map(str.strip, sys.stdin.read().strip().split('\n'))

mapping = dict(tuple(r.split(" -> ")) for r in rules)


@lru_cache(maxsize=None)
def counts_between(a, b, times):
    if times == 0 or not (middle := mapping.get(a + b)):
        return tuple()

    middle = mapping[a+b]
    left = counts_between(a, middle, times - 1)
    right = counts_between(middle, b, times - 1)

    result = Counter({middle: 1})
    result.update(dict(left))
    result.update(dict(right))

    return sorted(result.items())


def count_expanded_letters(polymer, times):
    counts = Counter()
    for i in range(len(polymer) - 1):
        counts[polymer[i]] += 1
        counts.update(dict(counts_between(polymer[i], polymer[i+1], times)))
    counts[polymer[-1]] += 1
    return counts


counts = sorted(count_expanded_letters(polymer, 40).items(), key=itemgetter(1))

print(counts[-1][1] - counts[0][1])
