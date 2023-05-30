from collections import defaultdict


class Solution:

    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        curr = defaultdict(int)
        ans = l = 0
        for r, c in enumerate(s):
            curr[c] += 1
            while len(curr) > k:
                curr[s[l]] -= 1
                if not curr[s[l]]:
                    del curr[s[l]]
                l += 1
            if len(curr) <= k:
                ans = max(ans, (r - l) + 1)
        return ans
