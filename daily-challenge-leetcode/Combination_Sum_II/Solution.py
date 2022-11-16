class Solution(object):
    def combinationSum2(self, c, target):
        c.sort()
        ans = []

        def backtrack(comb, j, s):
            if s == target:
                ans.append(comb)
                return
            last = -1
            for i in range(j, len(c)):
                if c[i] == last:
                    continue
                if s + c[i] > target:
                    return
                backtrack(comb + [c[i]], i + 1, s + c[i])
                last = c[i]

        backtrack([], 0, 0)
        return ans
