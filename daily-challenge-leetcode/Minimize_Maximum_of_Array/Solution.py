from typing import List


class Solution:

    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        # l,r = min(nums),max(nums)
        # def check(target):
        #     carry = 0
        #     for i in range(n-1,-1,-1):
        #         curr = nums[i] + carry
        #         if curr <= target:
        #             carry = 0
        #         else:
        #             carry = curr - target
        #     return carry

        # while l < r:
        #     m = (l+r)//2
        #     if not check(m) :
        #         r = m
        #     else:
        #         l = m + 1
        # return l
        ans = distribution = curr = 0
        for i in range(n):
            curr += nums[i]
            distribution += 1
            ans = max(ans, ceil(curr / distribution))
        return ans