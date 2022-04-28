from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left(nums, target) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            if nums[left] == target:
                return left
            return -1

        def find_right(nums, target) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if target >= nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            if nums[right] == target:
                return right
            return -1

        if len(nums) == 0 or target > nums[len(nums) - 1]:
            return [-1, -1]
        return [find_left(nums, target), find_right(nums, target)]
