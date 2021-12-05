import sys

first_line, *lines = sys.stdin.read().strip().split('\n')

nums = list(map(int, first_line.split(',')))

boards = []
marked_maps = []

for i in range(1, len(lines), 6):
    board = []
    marked_map = []
    for j in range(5):
        board.append(list(map(int, lines[i+j].split())))
        marked_map.append([False for _ in range(5)])

    boards.append(board)
    marked_maps.append(marked_map)


def mark_board(board, marked_map, num):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                marked_map[i][j] = True


def check_bingo(marked_map):
    # Row
    for row in marked_map:
        if all(row):
            return True

    # Column
    for j in range(5):
        if all(marked_map[i][j] for i in range(5)):
            return True


def calculate_score(board, marked_map):
    score = 0

    for i in range(5):
        for j in range(5):
            if not marked_map[i][j]:
                score += board[i][j]

    return score

winning_board_indexes = set()

for num in nums:
    for i in range(len(boards)):
        if i not in winning_board_indexes:
            mark_board(boards[i], marked_maps[i], num)

    for i in range(len(boards)):
        if i not in winning_board_indexes and check_bingo(marked_maps[i]):
            winning_board_indexes.add(i)
            last_winning_board_index = i
            last_num = num


score = calculate_score(
    boards[last_winning_board_index],
    marked_maps[last_winning_board_index],
)
print(score * last_num)
