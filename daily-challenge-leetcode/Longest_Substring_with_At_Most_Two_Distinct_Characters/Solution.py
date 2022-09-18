from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        current = defaultdict(int)
        best_lenght = 0
        l, r = 0, 0
        while r < len(s):
            current[s[r]] += 1
            if len(current) < 3:
                best_lenght = max(best_lenght, r - l)
            else:
                current[s[l]] -= 1
                if current[s[l]] < 1:
                    current.pop(s[l])
                l += 1
            r += 1
        return best_lenght + 1
