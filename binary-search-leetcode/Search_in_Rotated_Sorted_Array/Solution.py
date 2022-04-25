from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lenght = len(nums)

        def find_rotation():
            left = 0
            right = lenght - 1
            while nums[left] > nums[right]:
                mid = (left + right) // 2
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
            return left

        def rotate(index: int):
            return (index + shift) % lenght

        shift = find_rotation()
        left = 0
        right = lenght - 1
        while (right != 0 or left != lenght - 1) and nums[rotate(left)] < nums[rotate(right)]:
            mid = (left + right) // 2
            rotated_mid = rotate(mid)
            if nums[rotated_mid] == target:
                return rotated_mid
            if target > nums[rotated_mid]:
                left = mid + 1
            else:
                right = mid
        if nums[rotate(left)] == target:
            return rotate(left)
        return -1
