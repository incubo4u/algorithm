class Solution:
    def minimumTotal(self, T) -> int:
        INF = 10**5
        for i in range(1, len(T)):
            for j in range(len(T[i])):
                left = T[i - 1][j - 1] if 0 <= j - 1 < len(T[i - 1]) else INF
                right = T[i - 1][j] if 0 <= j < len(T[i - 1]) else INF
                T[i][j] += min(left, right)
        return min(T[-1])
