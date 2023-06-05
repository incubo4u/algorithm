class Solution:

    def checkStraightLine(self, cord: list[list[int]]) -> bool | None:
        (x1, y1), (x, y) = cord[0], cord[1]
        slope = (y1 - y) / (x1 - x) if x1 != x else -1
        for i in range(2, len(cord)):
            (x1, y1), (x, y) = cord[i - 1], cord[i]
            s = (y1 - y) / (x1 - x) if x1 != x else -1
            if slope != s:
                return
        return True
