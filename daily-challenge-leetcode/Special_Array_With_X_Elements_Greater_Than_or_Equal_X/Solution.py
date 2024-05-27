class Solution:

    def specialArray(self, nums: List[int]) -> int:
        prev = -1
        n = len(nums)
        for i, nr in enumerate(sorted(nums)):
            if (nr_left := n - i) <= prev:
                return -1

            if nr_left <= nr:
                return nr_left

            prev = nr
        return -1
