from collections import deque
from typing import List


class Solution:

    def compress(self, chars: List[str]) -> int:
        r = t = l = 0
        while r < len(chars):
            if chars[l] == chars[r]:
                t += 1
            elif chars[l] != chars[r] and t > 1:
                t = deque(str(t))
                while t:
                    l += 1
                    chars[l] = t.popleft()
                t = 1
                l += 1
                while l != r:
                    r -= 1
                    chars.pop(l)
            elif chars[l] != chars[r] and t <= 1:
                l = r
            r += 1
        if t > 1:
            for _ in range(t - 1):
                chars.pop()
            chars.extend(list(str(t)))

        return len(chars)
