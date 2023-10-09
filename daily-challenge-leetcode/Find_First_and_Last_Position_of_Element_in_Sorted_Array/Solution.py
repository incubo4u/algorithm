from bisect import bisect_left, bisect_right


class Solution:

    def searchRange(self, nums: list[int], target: int) -> tuple|list[int]:
        return (l, r - 1) if (l := bisect_left(
            nums, target)) != (r := bisect_right(nums, target)) else (-1, -1)
