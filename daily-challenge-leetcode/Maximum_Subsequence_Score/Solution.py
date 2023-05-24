from heapq import heappop, heappush


class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        mult = 100000
        curr = ans = 0
        hq = []
        for i, (o, t) in enumerate(sorted(zip(nums1, nums2), key=lambda t: -t[1])):
            curr += o
            if i == k - 1:
                ans = curr * t
            elif i > k - 1:
                curr -= heappop(hq)
                ans = max(ans, curr * t)
            heappush(hq, o)
        return ans
