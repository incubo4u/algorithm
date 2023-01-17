from collections import Counter


class Solution:

    def minFlipsMonoIncr(self, s: str):
        ans = flips = Counter(s)['0']
        for c in s:
            if c == '0':
                flips -= 1
            else:
                flips += 1
            ans = min(ans, flips)
        return ans
