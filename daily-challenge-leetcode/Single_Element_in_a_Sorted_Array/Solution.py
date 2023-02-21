from typing import List


class Solution:

    def singleNonDuplicate(self, nums: List[int]) -> int:
        # return reduce(lambda a,b: a^b, nums)
        ans = 0
        for n in nums:
            ans ^= n
        return ans