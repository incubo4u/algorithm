from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        length = 9
        squares = [set() for i in range(length)]
        columns = [set() for i in range(length)]
        rows = [set() for i in range(length)]

        def place(i, j, nr):
            rows[i].add(board[i][j])
            columns[j].add(board[i][j])
            squares[sqrFromPos(i, j)].add(board[i][j])
            board[i][j] = nr

        def remove(i, j, nr):
            rows[i].remove(board[i][j])
            columns[j].remove(board[i][j])
            squares[sqrFromPos(i, j)].remove(board[i][j])
            board[i][j] = '.'

        def sqrFromPos(i, j):
            return i//3 * 3 + j//3

        def isValid(i, j, nr):
            return (
                nr not in rows[i] and
                nr not in columns[j] and
                nr not in squares[sqrFromPos(i, j)])

        def memo():
            nonlocal squares
            nonlocal columns
            nonlocal rows
            for i in range(length):
                for j in range(length):
                    if board[i][j] != '.':
                        rows[i].add(board[i][j])
                        columns[j].add(board[i][j])
                        squares[sqrFromPos(i, j)].add(board[i][j])
        end = False

        def backtrack(i, j):
            nonlocal end
            if i > length -1:
                end = True
                return
            if board[i][j] == '.':
                for nr in range(1, 10):
                    nr = str(nr)
                    if isValid(i, j, nr):
                        place(i, j, nr)
                        backtrack(i, j+1) if j < length - 1 else backtrack(i+1, 0)
                        if not end:
                            remove(i, j, nr)
            else:
                backtrack(i, j+1) if j < length-1 else backtrack(i+1, 0)

        memo()
        backtrack(0, 0)
