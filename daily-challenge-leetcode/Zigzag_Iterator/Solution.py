from collections import deque
from typing import List


class ZigzagIterator:

    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = deque(v1)
        self.v2 = deque(v2)
        self.flag = True

    def next(self) -> int:
        if self.flag and self.v1:
            self.flag = not self.flag
            return self.v1.popleft()
        elif self.v2:
            self.flag = not self.flag
            return self.v2.popleft()
        else:
            self.flag = not self.flag
            return self.next()

    def hasNext(self) -> bool:
        return self.v1 or self.v2  # type: ignore


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())