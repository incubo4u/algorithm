from cmath import inf
from collections import Counter


class Solution:

    def balancedString(self, s: str) -> int:
        n = len(s)
        req = n / 4
        ans = inf
        count = Counter(s)
        extra = {}
        for _, (c, freq) in enumerate(count.items()):
            if freq > req:
                extra[c] = freq - req
        distinct = len(extra)
        if not distinct:
            return 0
        l = 0
        for r in range(n):
            if s[r] in extra:
                extra[s[r]] -= 1
                if not extra[s[r]]:
                    distinct -= 1

            while not distinct and l <= r:
                ans = min(r - l + 1, ans)
                if s[l] in extra:
                    extra[s[l]] += 1
                    if extra[s[l]] == 1:
                        distinct += 1
                l += 1
        return ans
