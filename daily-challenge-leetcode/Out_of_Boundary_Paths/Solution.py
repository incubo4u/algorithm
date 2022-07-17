# from functools import lru_cache


# class Solution:
#     def findPaths(
#         self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
#     ) -> int:
#         @lru_cache(None)
#         def find(move, y, x):
#             if y == m or y < 0 or x < 0 or x == n:
#                 return 1
#             if move == 0:
#                 return 0
#             move -= 1

#             return (
#                 find(move, y + 1, x)
#                 + find(move, y, x + 1)
#                 + find(move, y - 1, x)
#                 + find(move, y, x - 1)
#             ) % ((10**9) + 7)

#         return find(maxMove, startRow, startColumn)
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = {}
        yBound = range(0, m)
        xBound = range(0, n)
        directions = [(-1, 0), (0, +1), (+1, 0), (0, -1)]

        def find(x, y, move):
            if (x, y, move) in memo:
                return memo[(x, y, move)]
            if x not in xBound or y not in yBound:
                return 1
            if move == 0:
                return 0
            answear = 0
            for d in directions:
                answear += find(x + d[0], y + d[1], move - 1)
            memo[(x, y, move)] = answear
            return answear

        return find(startColumn, startRow, maxMove) % (10**9 + 7)
