class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        l1, l2 = len(t1), len(t2)
        mat = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        for i in range(l1 - 1, -1, -1):
            for j in range(l2 - 1, -1, -1):
                if t1[i] == t2[j]:
                    mat[i][j] = 1 + mat[i + 1][j + 1]
                else:
                    mat[i][j] = max(mat[i + 1][j], mat[i][j + 1])
        return mat[0][0]
