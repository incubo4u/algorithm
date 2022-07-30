from collections import Counter
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = [[], [], [], [], [], [], [], [], []]
        collumn = set()

        for i in range(9):
            if i < 3:
                squares[0].extend(board[i][:3])
                squares[1].extend(board[i][3:6])
                squares[2].extend(board[i][6:])
            elif 3 <= i < 6:
                squares[3].extend(board[i][:3])
                squares[4].extend(board[i][3:6])
                squares[5].extend(board[i][6:])
            else:
                squares[6].extend(board[i][:3])
                squares[7].extend(board[i][3:6])
                squares[8].extend(board[i][6:])
        
            counter = Counter(board[i])
            common = list(counter.most_common())
            if common[0][0] == '.':
                common.pop(0)
            if len(common) > 0 and common[0][1] > 1:
                return False

            for j in range(9):
                c = board[j][i]
                if c == '.':
                    continue
                if c not in collumn:
                    collumn.add(c)
                else:
                    return False
            collumn.clear()
        
        for counter in map(Counter, squares):
            common = list(counter.most_common())
            if common[0][0] == '.':
                common.pop(0)
            if len(common) > 0 and common[0][1] > 1:
                return False
        return True
