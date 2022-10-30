from math import ceil
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        lenght = m * n
        l, r = 0, lenght - 1
        i, j = 0, 0
        while l <= r:
            mid = (l + r) // 2
            i = ceil(mid // n)
            j = mid % n
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                l = mid + 1
            else:
                r = mid - 1
        return matrix[i][j] == target
