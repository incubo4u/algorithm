from collections import defaultdict
from heapq import heappop, heappush


class Solution:

    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        hq, ans = [], []
        count = defaultdict(int)

        for i, nr in enumerate(nums):
            nr *= -1
            if i <= k - 1:
                count[nr] += 1
                heappush(hq, nr)

            if i == k - 1:
                ans.append(-hq[0])

            if i > k - 1:
                count[-nums[i - k]] -= 1
                while hq and not count[hq[0]]:
                    heappop(hq)
                heappush(hq, nr)
                count[nr] += 1
                ans.append(-hq[0])

        return ans
