class Solution:
    def combinationSum(self, c, target):
        ans = []

        def backtrack(j, comb, s):
            if s == target:
                ans.append(comb)
                return
            elif s > target:
                return
            for i, nr in enumerate(c[j:], j):
                backtrack(i, comb + [nr], s + nr)

        backtrack(0, [], 0)
        return ans
