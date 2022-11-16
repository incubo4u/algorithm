from typing import Counter, List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        d = Counter(nums)
        res = []

        def backtrack(perm, choice):
            if len(perm) == len(nums):
                res.append(perm)
                return
            for i, key in enumerate(choice):
                if not choice[key]:
                    continue
                choice[key] -= 1
                backtrack(perm + [key], choice.copy())
                choice[key] += 1

        backtrack([], d)
        return res
