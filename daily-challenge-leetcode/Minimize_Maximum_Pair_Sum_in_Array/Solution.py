from math import inf


class Solution:

    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        i, j, ans = 0, len(nums) - 1, -inf
        while i < j:
            ans = max(nums[i] + nums[j], ans)
            i += 1
            j -= 1
        return ans
