from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        l = m = ans = 0
        freq = defaultdict(int)
        for r, nr in enumerate(nums):
            freq[nr] += 1
            while len(freq) > k:
                freq[nums[l]] -= 1
                if not freq[nums[l]]:
                    del freq[nums[l]]
                l += 1
                m = l
            while freq[nums[l]] > 1:
                freq[nums[l]] -= 1
                l += 1
            ans += ((l - m) + 1) * int(len(freq) == k)
        return ans
