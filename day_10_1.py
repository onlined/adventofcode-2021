import sys


CHAR_TO_POINT = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

CLOSE_TO_OPEN = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}


def get_first_illegal_char(text):
    stack = []
    for ch in text:
        if ch in CLOSE_TO_OPEN:
            if stack and stack[-1] == CLOSE_TO_OPEN[ch]:
                stack.pop()
            else:
                return ch
        else:
            stack.append(ch)

    return None


lines = map(str.strip, sys.stdin.read().strip().split('\n'))




total = 0
for line in lines:
    total += CHAR_TO_POINT.get(get_first_illegal_char(line), 0)

print(total)

