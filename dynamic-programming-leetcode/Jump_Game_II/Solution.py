from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r, ans = 0, 0, 0
        while r < len(nums) - 1:
            r_most = 0
            for jmp_i in range(l, r + 1):
                r_most = max(jmp_i + nums[jmp_i], r_most)
            l = r + 1
            r = r_most
            ans += 1
        return ans
