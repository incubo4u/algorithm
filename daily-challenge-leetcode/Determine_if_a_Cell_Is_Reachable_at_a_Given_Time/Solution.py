class Solution:

    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int,
                          t: int) -> bool:
        return max(abs(sx - fx), abs(sy - fy)) <= t and not (
            (fx, fy) == (sx, sy) and t == 1)
