from collections import defaultdict
from typing import List


class Solution:

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sn = ans = 0
        m = defaultdict(int)
        m[0] = 1
        for i, n in enumerate(nums):
            sn += n
            ans += m[sn % k]
            m[sn % k] += 1
        return ans
