import sys
from operator import itemgetter
import heapq
import copy

lines = map(str.strip, sys.stdin.read().strip().split('\n'))
cavern = [list(map(int, list(l))) for l in lines]

def get_risk(i, j):
    risk = cavern[i % len(cavern)][j % len(cavern[0])]
    risk += i // len(cavern) + j // len(cavern[0])
    risk %= 9
    if risk == 0:
        risk = 9
    return risk


rows = 5 * len(cavern)
cols = 5 * len(cavern[0])
min_risks = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(float('inf'))
    min_risks.append(row)


heap = [(0, (0, 0))]
while heap:
    risk, (i, j) = heapq.heappop(heap)

    if (i, j) == (rows - 1, cols - 1):
        if risk < min_risks[-1][-1]:
            min_risks[-1][-1] = risk
        continue

    if risk >= min_risks[i][j]:
        continue
    min_risks[i][j] = risk

    if i < rows - 1:
        heapq.heappush(heap, (risk + get_risk(i+1, j), (i+1, j)))
    if j < cols - 1:
        heapq.heappush(heap, (risk + get_risk(i, j+1), (i, j+1)))
    if i > 0:
        heapq.heappush(heap, (risk + get_risk(i-1, j), (i-1, j)))
    if j > 0:
        heapq.heappush(heap, (risk + get_risk(i, j-1), (i, j-1)))



print(min_risks[-1][-1])

