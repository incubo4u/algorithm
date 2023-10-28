class Solution:

    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for length in range(n):
            for j in range(length, n):
                ans += len(set(nums[j - length:j + 1]))**2
        return ans
