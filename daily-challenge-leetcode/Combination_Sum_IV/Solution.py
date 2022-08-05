from typing import List


class Solution:
    # TLE
    # def combinationSum4(self, nums: List[int], target: int) -> int:
    #     ret = 0
    #     def backtrack(rest):
    #         nonlocal ret
    #         if rest == 0:
    #             ret+=1
    #             return
    #         for i , nr in enumerate(nums):
    #             if nr <= rest:
    #                 backtrack(rest-nr)
    #     backtrack(target)
    #     return ret

    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {0: 1}
        for total in range(1, target + 1):
            cache[total] = 0
            for n in nums:
                cache[total] += cache.get(total - n, 0)
        return cache[total]
