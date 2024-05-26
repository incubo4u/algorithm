class Solution:

    def checkRecord(self, n: int) -> int:
        MOD = (10**9) + 7
        ways = [[[0] * 4 for a in range(3)] for d in range(n + 1)]

        for absence in range(2):
            for late in range(3):
                ways[-1][absence][late] = 1

        for day in reversed(range(n)):
            for absence in reversed(range(2)):
                for late in reversed(range(3)):
                    ways[day][absence][late] = (
                        # present and not late
                        ways[day + 1][absence][0] % MOD +
                        # not present => not late too
                        ways[day + 1][absence + 1][0] % MOD +
                        # late => present
                        ways[day + 1][absence][late + 1] % MOD) % MOD
        return ways[0][0][0] % MOD
