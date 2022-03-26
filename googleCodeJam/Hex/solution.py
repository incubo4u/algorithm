def game_status(lenght, board):
    def count_colors():
        r, b = 0, 0
        for i in board:
            for j in i:
                if j == "B":
                    b += 1
                if j == "R":
                    r += 1
        return r, b

    def add_padding():
        board.append(["R" for i in range(lenght)])
        board.insert(0, ["R" for i in range(lenght)])
        for i in range(lenght + 2):
            board[i].append("B")
            board[i].insert(0, "B")

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

    def blue_path_from_corner(left, right, left_boundary, right_boundary):
        path = set()
        while left[1] < left_boundary:
            path.add(left)
            left, right = step("B", left, right)
            if right[0] == right_boundary:
                return None
        return path

    def red_path_from_corner(left, right, left_boundary, right_boundary):
        path = set()
        while left[0] > left_boundary:
            path.add(left)
            left, right = step("R", left, right)
            if right[1] == right_boundary:
                return None
        return path

    red_moves, blue_moves = count_colors()
    if abs(red_moves - blue_moves) > 1:
        return "Impossible"
    add_padding()
    lenght += 2
    directions = [(0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1), (1, 0)]
    left, right = (lenght - 1, 0), (lenght - 1, 1)
    first_path = blue_path_from_corner(left, right, lenght - 1, 0)
    if first_path:
        directions.reverse()
        left, right = (0, 0), (0, 1)
        second_path = blue_path_from_corner(left, right, lenght - 1, lenght - 1)
        common = first_path.intersection(second_path)
        directions.reverse()
        if common and blue_moves >= red_moves:
            return "Blue wins"
        return "Impossible"
    left, right = (lenght - 1, lenght - 1), (lenght - 2, lenght - 1)
    first_path = red_path_from_corner(left, right, 0, 0)
    if first_path:
        directions.reverse()
        left, right = (lenght - 1, 0), (lenght - 2, 0)
        second_path = red_path_from_corner(left, right, 0, lenght - 1)
        common = first_path.intersection(second_path)
        if common and red_moves >= blue_moves:
            return "Red wins"
        return "Impossible"
    return "Nobody wins"


def main():
    test_cases = int(input())
    for test_case in range(1, test_cases + 1, 1):
        lenght = int(input())
        board = []
        for _ in range(lenght):
            board.append(list(input().strip()))
        ans = game_status(lenght, board)
        print("Case #{}: {}".format(test_case, ans))


if __name__ == "__main__":
    main()
