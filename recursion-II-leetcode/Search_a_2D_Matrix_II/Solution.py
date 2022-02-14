from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def find(x, y):
            if y < 0 or x > len(matrix)-1:
                return False
            if matrix[x][y] == target:
                return True
            if matrix[x][y] > target:
                return find(x, y-1)
            else:
                return find(x+1, y)
        return find(0, len(matrix[0])-1)
