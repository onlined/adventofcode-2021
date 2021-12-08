import sys

lines = sys.stdin.read().strip().split('\n')

total = 0

for line in lines:
    single_digits, displayed_digits = (list(map(frozenset, p.split(' '))) for p in line.split(' | '))

    seg2dig = {}
    dig2seg = {}
    for digit, seg_count in ((1, 2), (4, 4), (7, 3), (8, 7)):
        dig2seg[digit] = next(d for d in single_digits if len(d) == seg_count)
        seg2dig[dig2seg[digit]] = digit

    for seg in dig2seg[1]:
        not_having_seg = [d for d in single_digits if seg not in d]
        if len(not_having_seg) == 1:
            bottom_right_seg = seg
            dig2seg[2] = not_having_seg[0]
            seg2dig[dig2seg[2]] = 2
        else:
            top_right_seg = seg

    dig2seg[6] = next(d for d in single_digits if set(d) == set(dig2seg[8]) - {top_right_seg})
    seg2dig[dig2seg[6]] = 6

    top_left_seg = next(iter(set(dig2seg[8]) - set(dig2seg[2]) - {bottom_right_seg}))
    dig2seg[3] = next(d for d in single_digits if not top_left_seg in d and d not in seg2dig)
    seg2dig[dig2seg[3]] = 3

    dig2seg[5] = next(d for d in single_digits if len(d) == 5 and d not in seg2dig)
    seg2dig[dig2seg[5]] = 5

    bottom_left_seg = next(iter(set(dig2seg[6]) - set(dig2seg[5])))
    dig2seg[0] = next(d for d in single_digits if bottom_left_seg in d and d not in seg2dig)
    seg2dig[dig2seg[0]] = 0

    dig2seg[9] = next(d for d in single_digits if d not in seg2dig)
    seg2dig[dig2seg[9]] = 9

    num = 0
    for d in displayed_digits:
        num = num * 10 + seg2dig[d]
    total += num


print(total)

