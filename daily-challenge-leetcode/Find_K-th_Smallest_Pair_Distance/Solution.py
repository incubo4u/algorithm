# Runtime Percentile: 79.14370000000001
# Memory Percentile: 67.26520000000001


class Solution:

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        l, r = 0, nums[n - 1]
        while l < r:
            guess = (l + r) // 2
            lo = pairs = 0
            for hi in range(1, n):
                while nums[hi] - nums[lo] > guess:
                    lo += 1
                pairs += hi - lo
            if pairs >= k:
                r = guess
            else:
                l = guess + 1
        return l
