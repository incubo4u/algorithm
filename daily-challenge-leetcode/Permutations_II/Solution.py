from typing import Counter, List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        choice = Counter(nums)
        res = []

        def backtrack(perm):
            if len(perm) == len(nums):
                res.append(perm)
                return
            for i, key in enumerate(choice):
                if not choice[key]:
                    continue
                choice[key] -= 1
                backtrack(perm + [key])
                choice[key] += 1

        backtrack([])
        return res
