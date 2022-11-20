from functools import reduce
from itertools import product


class Solution:
    def exist(self, board, word):
        def dfs(wi, i, j):
            if wi == w:
                return True

            if i < 0 or i >= m or j < 0 or j >= n:
                return

            if board[i][j] != word[wi]:
                return

            board[i][j] = "x"

            for x, y in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
                if dfs(wi + 1, i + x, j + y):
                    return True
            
            board[i][j] = word[wi]

        m, n, w = len(board), len(board[0]), len(word)
        if set(word) - reduce(lambda a, b: a | b, map(set, board)):
            return False
        for i, j in product(range(m), range(n)):
            if board[i][j] != word[0]:
                continue
            if dfs(0, i, j):
                return True
