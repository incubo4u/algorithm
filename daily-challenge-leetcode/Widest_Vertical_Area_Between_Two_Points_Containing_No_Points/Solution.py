class Solution:

    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        l = points[0][0]
        ans = 0
        for r, _ in points:
            ans = max(ans, r - l)
            l = r
        return ans
