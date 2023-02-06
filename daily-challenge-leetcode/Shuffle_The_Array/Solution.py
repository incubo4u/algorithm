from typing import List


class Solution:

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for _, (a, b) in enumerate(zip(nums[:n], nums[n:])):
            ans.append(a)
            ans.append(b)
        return ans