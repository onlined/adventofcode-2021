import sys
from collections import Counter
from operator import itemgetter

polymer, _, *rules = map(str.strip, sys.stdin.read().strip().split('\n'))

mapping = dict(tuple(r.split(" -> ")) for r in rules)


def apply_mapping(polymer):
    new_polymer = []
    for i in range(len(polymer) - 1):
        new_polymer.append(polymer[i])
        if to_insert := mapping.get(polymer[i:i+2]):
            new_polymer.append(to_insert)
    new_polymer.append(polymer[-1])
    return ''.join(new_polymer)


for _ in range(10):
    polymer = apply_mapping(polymer)


counts = sorted(Counter(polymer).items(), key=itemgetter(1))

print(counts[-1][1] - counts[0][1])
