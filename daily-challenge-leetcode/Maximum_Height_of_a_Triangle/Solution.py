# Runtime Percentile: 62.14559999999999
# Memory Percentile: 6.397699999999983


class Solution:

    def maxHeightOfTriangle(self, red: int, blue: int) -> int:

        def count(b, bb, h):
            if not b and not bb:
                return h - 1
            if b < 0 or bb < 0:
                return h - 2
            if h % 2:
                b -= h
            else:
                bb -= h
            return count(b, bb, h + 1)

        return max(count(red, blue, 1), count(blue, red, 1))
