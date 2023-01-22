from typing import List


class Solution:

    def partition(self, s: str) -> List[List[str]]:

        n = len(s)
        ans = []

        def backtrack(i, subs):
            if i > n - 1:
                ans.append(subs)
            for j in range(i, n):
                if (sub := s[i:j + 1]) == sub[::-1]:
                    backtrack(j + 1, subs + [sub])

        backtrack(0, [])
        return ans
