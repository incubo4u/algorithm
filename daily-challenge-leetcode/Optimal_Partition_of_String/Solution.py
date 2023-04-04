class Solution:

    def partitionString(self, s: str) -> int:
        seen = set()
        ans = 0
        for c in s:
            if c not in seen:
                seen.add(c)
            else:
                ans += 1
                seen.clear()
                seen.add(c)
        return ans + 1

