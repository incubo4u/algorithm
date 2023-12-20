class Solution:

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        seen_index = {}
        window_sum = ans = l = 0

        for r in range(n):
            if nums[r] in seen_index:
                last_seen_index = seen_index[nums[r]]
                for i in range(l, last_seen_index + 1):
                    del seen_index[nums[i]]
                    window_sum -= nums[i]
                l = last_seen_index + 1

            window_sum += nums[r]
            seen_index[nums[r]] = r

            if r - l + 1 > k:
                window_sum -= nums[l]
                del seen_index[nums[l]]
                l += 1

            if r - l + 1 == k:
                ans = max(window_sum, ans)

        return ans
