# Runtime Percentile: 74.53590000000023
# Memory Percentile: 65.7407


class Solution:

    def maxPoints(self, points: List[List[int]]) -> int:
        n, m = len(points), len(points[0])
        prev_row = points[0]

        for r in range(1, n):
            left = [0] * m
            right = [0] * m
            curr = [0] * m
            left[0] = prev_row[0]

            for c in range(1, m):
                left[c] = max(left[c - 1] - 1, prev_row[c])

            right[-1] = prev_row[-1]
            for c in reversed(range(m - 1)):
                right[c] = max(right[c + 1] - 1, prev_row[c])

            for c in range(m):
                curr[c] = points[r][c] + max(left[c], right[c])
            prev_row = curr

        return max(prev_row)
