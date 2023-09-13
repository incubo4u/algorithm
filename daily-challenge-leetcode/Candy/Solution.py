from typing import List


class Solution:

    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ans = 0
        candy = [0] * n
        for i, r in sorted(enumerate(ratings), key=lambda t: t[1]):
            c = 1
            if i + 1 < n and ratings[i + 1] < r:
                c = max(candy[i + 1] + 1, c)
            if i - 1 > -1 and ratings[i - 1] < r:
                c = max(candy[i - 1] + 1, c)
            candy[i] = c
            ans += c
        return ans
