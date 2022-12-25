from typing import List


class Solution:

    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = [0] * len(queries)
        for i, q in enumerate(queries):
            s = 0
            for n in sorted(nums):
                s += n
                if s > q:
                    break
                ans[i] += 1
        return ans
