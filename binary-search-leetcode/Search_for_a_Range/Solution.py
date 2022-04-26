from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lenght = len(nums)

        def find():
            left, right = 0, lenght - 1
            while left <= right:
                if left == right and nums[left] != target:
                    return -1
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            return -1

        start = end = find()
        if start == -1:
            return [-1, -1]
        while start > 0 and nums[start - 1] == target:
            start -= 1
        while end < lenght - 1 and nums[end + 1] == target:
            end += 1

        return [start, end]
