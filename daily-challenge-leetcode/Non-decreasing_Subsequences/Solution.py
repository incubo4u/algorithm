class Solution:

    def findSubsequences(self, nums):
        n = len(nums)
        ans = set()

        def backtrack(i, curr):

            for j in range(i, n):
                if not curr or curr[-1] <= nums[j]:
                    backtrack(j + 1, curr + [nums[j]])
            if len(curr) >= 2:
                ans.add(tuple(curr))

        backtrack(0, [])
        return ans
