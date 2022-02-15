class Solution:
    def __init__(self) -> None:
        self.rows = -1
        self.hills = set()
        self.dales = set()
        self.cols = set()

    def placeQueen(self, x, y) -> None:
        self.cols.add(x)
        self.dales.add(y-x)
        self.hills.add(y+x)
        self.rows += 1

    def isSafePosition(self, x, y) -> bool:
        return (x not in self.cols and
                y > self.rows and
                y-x not in self.dales and
                y+x not in self.hills)

    def removeQueen(self, x, y):
        self.cols.remove(x)
        self.dales.remove(y-x)
        self.hills.remove(y+x)
        self.rows -= 1

    def totalNQueens(self, n) -> int:
        def tnq(row, count):
            for col in range(n):
                if self.isSafePosition(col, row):
                    self.placeQueen(col, row)
                    if row + 1 == n:
                        count += 1
                    else:
                        count = tnq(row+1, count)
                    self.removeQueen(col, row)
            return count
        return tnq(0, 0)
