from typing import List


class Solution:

    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ans = 0
        for _, c in enumerate(sorted(costs)):
            coins -= c
            if coins < 0:
                break
            ans += 1
        return ans