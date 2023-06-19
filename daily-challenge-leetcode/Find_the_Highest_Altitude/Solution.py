class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        ans = h = 0
        for g in gain:
            h += g
            ans = max(h, ans)
        return ans
