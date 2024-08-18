# Runtime Percentile: 16.247100000000085
# Memory Percentile: 18.3752


class Solution:

    def nthUglyNumber(self, n: int) -> int:
        seen = set()
        hq = [1]
        while len(seen) < n:
            if (nr := heappop(hq)) in seen:
                continue
            seen.add(nr)
            if (two := nr * 2) not in seen:
                heappush(hq, two)
            if (three := nr * 3) not in seen:
                heappush(hq, three)
            if (five := nr * 5) not in seen:
                heappush(hq, five)
        return nr
