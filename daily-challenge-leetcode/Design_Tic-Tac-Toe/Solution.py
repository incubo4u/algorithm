from collections import defaultdict


class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.diag_left, self.diag_right = defaultdict(int), defaultdict(int)
        self.vertical, self.horizontal = defaultdict(int), defaultdict(int)

    def move(self, row: int, col: int, player: int) -> int:
        d_l_key, d_r_key = (row - col, player), (col + row, player)
        v_key, h_key = (col, player), (row, player)
        self.diag_left[d_l_key] += 1
        self.diag_right[d_r_key] += 1
        self.vertical[v_key] += 1
        self.horizontal[h_key] += 1
        if (
            self.diag_left[d_l_key] == self.n
            or self.diag_right[d_r_key] == self.n
            or self.vertical[v_key] == self.n
            or self.horizontal[h_key] == self.n
        ):
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
