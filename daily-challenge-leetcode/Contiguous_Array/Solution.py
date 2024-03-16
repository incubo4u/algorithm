class Solution:

    def findMaxLength(self, nums: List[int]) -> int:
        ans = s = 0
        prefix = {0: -1}
        for i, nr in enumerate(nums):
            s += 1 if nr else -1
            if s not in prefix:
                prefix[s] = i
            if s in prefix:
                ans = max(ans, (i - prefix[s]))
        return ans
