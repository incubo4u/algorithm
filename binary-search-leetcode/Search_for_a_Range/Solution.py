from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left(nums, target) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                if left == right and nums[left] == target:
                    return left
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] == target:
                    right = mid
                else:
                    right = mid - 1
            return -1

        def find_right(nums, target) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                if left == right or left + 1 == right:
                    if nums[right] == target:
                        return right
                    if nums[left] == target:
                        return left
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] == target:
                    left = mid
                else:
                    right = mid - 1
            return -1

        if len(nums) == 0:
            return [-1, -1]
        return [find_left(nums, target), find_right(nums, target)]
