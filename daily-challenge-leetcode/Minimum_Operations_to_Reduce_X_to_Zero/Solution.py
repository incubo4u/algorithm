class Solution:

    def minOperations(self, nums, x: int) -> int:
        n = len(nums)
        s = l = 0
        ans = -1
        limit = (nums_sum := sum(nums)) - x

        if min(nums) > x:
            return -1

        if nums_sum == x:
            return n

        for r in range(n):
            s += nums[r]
            while limit < s and l < r:
                s -= nums[l]
                l += 1

            if limit == s:
                ans = max(ans, (r - l) + 1)

        return n - ans if ans != -1 else ans
