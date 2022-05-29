from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        def find(l, r):
            m = (l + r) // 2
            if l >= r:
                return nums[l]
            if nums[l] == nums[r] == nums[m]:
                return min(find(l + 1, m - 1), find(m + 1, r - 1))
            if nums[m] > nums[r]:
                return find(m + 1, r)
            else:
                return find(l, m)

        return find(left, right)
