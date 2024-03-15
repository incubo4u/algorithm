class Solution:

    def numSubarraysWithSum(self, nums: List[int], g: int) -> int:
        n = len(nums)
        ans = s = 0
        freq = {}
        for i in range(n):
            s += nums[i]
            ans += int(s == g)
            ans += freq.get(s - g, 0)
            freq[s] = freq.get(s, 0) + 1
        return ans
