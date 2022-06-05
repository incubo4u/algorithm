from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        one = set(nums1)
        two = set(nums2)
        return one.intersection(two)
    ## worst solution but with bin search
    # def intersection(self, nums1, nums2):
    #     def find_in_nums1(target):
    #         left, right = 0, len(nums1) - 1
    #         while left < right:
    #             mid = (left + right) // 2
    #             if nums1[mid] < target:
    #                 left = mid + 1
    #             else:
    #                 right = mid
    #         if nums1[left] == target:
    #             return True
    #         return False

    #     nums1.sort()
    #     result = set()
    #     for i in nums2:
    #         if find_in_nums1(i) and i not in result:
    #             result.add(i)
    #     return result
