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


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        lenght = len(nums)

        def swap(x, o):
            nums[x], nums[o] = nums[o], nums[x]

        def backtrack(j):
            if j == lenght-1:
                result.append(nums[:])
            for i in range(lenght):
                if j <= i:
                    swap(j, i)
                    backtrack(j+1)
                    swap(j, i)

        backtrack(0)
        return result
