class Solution:
    def minDifficulty(self, job_diff, d: int) -> int:
        N = len(job_diff)
        if N < d:
            return -1
        INF = 10**20
        has_cache = [[False] * (d + 1) for _ in range(N + 1)]
        cache = [[None] * (d + 1) for _ in range(N + 1)]

        def backtrack(j, splits):
            if j == N:
                if splits < 1:
                    return 0
                return INF
            if splits == 0:
                return INF
            if has_cache[j][splits]:
                return cache[j][splits]
            best, max_diff = INF, 0
            for i in range(j, N):
                max_diff = max(max_diff, job_diff[i])
                best = min(best, backtrack(i + 1, splits - 1) + max_diff)
            has_cache[j][splits] = True
            cache[j][splits] = best
            return best

        return backtrack(0, d)
