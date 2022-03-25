
def game_status(board_size, board):
    def count_colors():
        r, b = 0, 0
        for i in board:
            for j in i:
                if j == 'B':
                    b += 1
                if j == 'R':
                    r += 1
        return r, b

    def add_padding():
        nonlocal board, board_size
        board.append(['R' for i in range(board_size)])
        board.insert(0, ['R' for i in range(board_size)])
        for i in range(board_size+2):
            board[i].append('B')
            board[i].insert(0, 'B')

    def get_next_hex(left, right):
        right_dir = (right[0] - left[0], right[1] - left[1])
        for index, direction in enumerate(directions):
            if right_dir == direction:
                next_dir = directions[(index + 1) % 6]
                return (left[0] + next_dir[0], left[1] + next_dir[1])
        raise Exception

    def step(colour, left, right):
        next_hex = get_next_hex(left, right)
        if board[next_hex[0]][next_hex[1]] == colour:
            return next_hex, right
        else:
            return left, next_hex

    def find_southwest_red_path():
        nonlocal board
        left, right = (board_size - 1, 0), (board_size - 2, 0)
        path = set()
        while left[0] > 0:
            path.add(left)
            left, right = step('R', left, right)
            if right[1] == board_size - 1:
                return None
        return path

    def find_southeast_red_path():
        nonlocal board
        left, right = (board_size - 1, board_size -
                       1), (board_size - 2, board_size - 1)
        path = set()
        while left[0] > 0:
            path.add(left)
            left, right = step('R', left, right)
            if right[1] == 0:
                return None
        return path

    def find_nothwest_blue_path():
        nonlocal board
        left, right = (0, 0), (0, 1)
        path = set()
        while left[1] < board_size - 1:
            path.add(left)
            left, right = step('B', left, right)
            if right[0] == board_size-1:
                return None
        return path

    def find_southwest_blue_path():
        nonlocal board
        left, right = (board_size - 1, 0), (board_size - 1, 1)
        path = set()
        while left[1] < board_size - 1:
            path.add(left)
            left, right = step('B', left, right)
            if right[0] == 0:
                return None
        return path

    red_moves, blue_moves = count_colors()
    if abs(red_moves - blue_moves) > 1:
        return 'Impossible'

    add_padding()
    board_size += 2
    #not clockwise
    directions = [(0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1), (1, 0)]
    southwest_blue_path = find_southwest_blue_path()
    if southwest_blue_path:
        # clockwise
        directions.reverse()
        nothwest_blue_path = find_nothwest_blue_path()
        intersection = southwest_blue_path.intersection(nothwest_blue_path)
        #not clockwise
        directions.reverse()
        if intersection and blue_moves >= red_moves:
            return 'Blue wins'
        else:
            return 'Impossible'

    southeast_red_path = find_southeast_red_path()
    if southeast_red_path:
        # clockwise
        directions.reverse()
        southwest_red_path = find_southwest_red_path()
        intersection = southeast_red_path.intersection(southwest_red_path)
        if intersection and red_moves >= blue_moves:
            return 'Red wins'
        else:
            return 'Impossible'
    return 'Nobody wins'


def main():
    test_cases = int(input())
    for test_case in range(1, test_cases + 1, 1):
        board_size = int(input())
        board = []
        for _ in range(board_size):
            board.append(list(input().strip()))
        ans = game_status(board_size, board)
        print('Case #{}: {}'.format(test_case, ans))


if __name__ == '__main__':
    main()
