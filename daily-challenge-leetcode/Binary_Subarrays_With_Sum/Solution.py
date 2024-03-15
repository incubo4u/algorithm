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

    def __numSubarraysWithSum(self, nums: List[int], g: int) -> int:
        n = len(nums)
        s = zero = ans = l = 0
        for r in range(n):
            s += nums[r]
            while l < r and (not nums[l] or s > g):
                zero = int(not nums[l]) * (zero + 1)
                s -= nums[l]
                l += 1
            ans += int(s == g) + (zero * int(s == g))
        return ans
