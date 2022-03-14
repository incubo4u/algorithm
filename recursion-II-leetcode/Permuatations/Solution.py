from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm, result = [], []
        lenght = len(nums)
        placed = [False for i in range(lenght)]

        def backtrack():
            if len(perm) == lenght:
                result.append(perm[:])
                return perm
            for i in range(lenght):
                if not placed[i]:
                    placed[i] = True
                    perm.append(nums[i])
                    backtrack()
                    placed[i] = False
                    perm.pop()
        backtrack()
        return result
