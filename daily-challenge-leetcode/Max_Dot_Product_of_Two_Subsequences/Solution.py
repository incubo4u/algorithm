class Solution:

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        INF = 1001

        # @cache
        # def get_max(i, j):
        #     if i > n - 1 or j > m - 1:
        #         return -INF
        #     return max(
        #         get_max(i + 1, j + 1) + (use := nums1[i] * nums2[j]),
        #         get_max(i + 1, j), get_max(i, j + 1), use)

        # return get_max(0, 0)

        dp = [[-INF] * (m + 1) for _ in range(n + 1)]
        dp[n][m] = 0
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                dp[i][j] = max(dp[i + 1][j + 1] + (use := nums1[i] * nums2[j]),
                               dp[i + 1][j], dp[i][j + 1], use)
        return dp[0][0]
