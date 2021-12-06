import sys

fish = list(map(int, sys.stdin.read().strip().split(',')))

for _ in range(80):
    new_fish = 0
    for i in range(len(fish)):
        if fish[i] == 0:
            fish[i] = 6
            new_fish += 1
        else:
            fish[i] -= 1

    fish.extend([8] * new_fish)


print(len(fish))
