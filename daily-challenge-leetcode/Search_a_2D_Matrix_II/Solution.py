from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows , collumns = len(matrix),len(matrix[0])
        x,y = rows-1,0
        while x >= 0 and y < collumns:
            if matrix[x][y] > target:
                x-=1
            elif matrix[x][y] < target:
                y+=1
            else:
                return True
        return False