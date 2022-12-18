from typing import List


class Solution:

    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        ans, s = [0] * len(temp), []
        for idx, t in enumerate(temp):
            while s and t > temp[s[-1]]:
                i = s.pop()
                ans[i] = idx - i
            s.append(idx)
        return ans
