def game_status(board_size, board):
    count_colors = {'B': 0, 'R': 0}
    visited = {}
    directions = [(-1, 0), (1, 0), (-1, 1), (1, -1), (0, -1), (0, 1)]
    winner = None

    def count_colors():
        for i in board:
            for j in i:
                if j != '.':
                    count_colors[j] += 1

    def too_many_moves():
        if winner:
            return (winner == 'B' and count_colors[0] < count_colors[1]) or (winner == 'R' and count_colors[1] < count_colors[0])
        return abs(count_colors['R'] - count_colors['B']) > 1

    def many_winning_road():
        pass

    def find_road(i, j):
        if winner or i not in range(board_size) or j not in range(board_size):
            return
        if board[i][j] == '.':
            return
        if visited.get((i, j)):
            return
        visited[(i, j)] = board[i][j]
        if (board[i][j] == 'B' and j == board_size - 1) or (board[i][j] == 'R' and i == board_size - 1):
            winner = board[i][j]
        else:
            for dir in directions:
                find_road(i+dir[0], j+dir[1])
        return winner

    count_colors()
    if too_many_moves():
        return 'Impossible'

    for i, (b, r) in enumerate(zip(board, board[0])):
        if winner:
            break
        if b == 'B':
            find_road(i, 0)
        if r == 'R':
            find_road(0, i)
    if not winner:
        return 'Nobody wins'
    if too_many_moves() or many_winning_road():
        return "Impossible"


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
