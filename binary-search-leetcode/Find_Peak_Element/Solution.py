from operator import le
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def bin_search_rec(left, right):
            if left == right:
                return left
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return bin_search_rec(left, mid)
            return bin_search_rec(mid + 1, right)

        def bin_search():
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > nums[mid + 1]:
                    right = mid
                else:
                    left = mid + 1
            return left

        # return bin_search_rec(0, len(nums) - 1)
        return bin_search()
