import bisect
from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        t = (timestamp, value)
        bisect.insort(self.d[key], t, key=lambda x: x[0])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        lenght = len(self.d[key])
        l, r = 0, lenght - 1
        while l < r:
            mid = (l + r) // 2
            v = self.d[key][mid][0]
            if v == timestamp:
                return self.d[key][mid][1]
            if v < timestamp:
                l += mid + 1
            else:
                r = mid
        if l > lenght:
            return self.d[key][-1][1]
        elif self.d[key][l][0] <= timestamp:
            return self.d[key][l][1]
        elif l > 0:
            return self.d[key][l - 1][1]
        else:
            return ""
