from typing import List


class Solution:
    # def findDuplicate(self, nums: List[int]) -> int:
    #     slowPtr = nums[0]
    #     fastPtr = nums[0]

    #     slowPtr = nums[slowPtr]
    #     fastPtr = nums[fastPtr]
    #     fastPtr = nums[fastPtr]
    #     while slowPtr != fastPtr:
    #         slowPtr = nums[slowPtr]
    #         fastPtr = nums[fastPtr]
    #         fastPtr = nums[fastPtr]
    #     lastPtr = nums[0]
    #     while slowPtr != lastPtr:
    #         slowPtr = nums[slowPtr]
    #         lastPtr = nums[lastPtr]
    #     return lastPtr
