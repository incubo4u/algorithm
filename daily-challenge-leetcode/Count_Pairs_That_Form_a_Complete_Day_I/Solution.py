# Runtime Percentile: 87.96209999999998
# Memory Percentile: 51.55829999999999


class Solution:

    def countCompleteDayPairs(self, hours: List[int]) -> int:
        seen = defaultdict(int)
        ans = 0
        for h in hours:
            ans += seen[h % 24]
            if not h % 24:
                ans += seen[24]
            seen[24 - (h % 24)] += 1
        return ans
