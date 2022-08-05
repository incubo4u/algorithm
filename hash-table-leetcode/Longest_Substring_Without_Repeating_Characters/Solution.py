class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = 0
        result = 0
        for end, char in enumerate(s):
            if char not in seen:
                result = max(result, end - start + 1)
            else:
                if seen[char] < start:
                    result = max(result, end - start + 1)
                else:
                    start = seen[char] + 1
            seen[char] = end
        return result
