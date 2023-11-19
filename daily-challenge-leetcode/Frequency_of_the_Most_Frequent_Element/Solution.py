class Solution:

    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 1
        curr_sum = left = 0
        for right in range(n):
            target = nums[right]
            curr_sum += target
            while target * (right - left + 1) - curr_sum > k:
                curr_sum -= nums[left]
                left += 1
            ans = max(right - left + 1, ans)
        return ans
