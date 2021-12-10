import sys


CHAR_TO_POINT = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

OPEN_TO_CLOSE = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def get_completion(text):
    stack = []
    for ch in text:
        if ch in OPEN_TO_CLOSE.values():
            if stack and OPEN_TO_CLOSE[stack[-1]] == ch:
                stack.pop()
            else:
                return None
        else:
            stack.append(ch)

    return [OPEN_TO_CLOSE[ch] for ch in reversed(stack)]


def calculate_score(completion):
    score_map = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }

    total = 0
    for ch in completion:
        total = total * 5 + score_map[ch]

    return total


lines = map(str.strip, sys.stdin.read().strip().split('\n'))

scores = []
for line in lines:
    compl = get_completion(line)
    if not compl:
        continue

    scores.append(calculate_score(compl))

scores.sort()
print(scores[len(scores)//2])
