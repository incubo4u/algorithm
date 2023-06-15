class Solution:

    def findMissingRanges(self, nums: list[int], lower: int,
                          upper: int) -> list[list[int]]:
        l = len(nums)
        if not nums:
            return [(lower, upper)]

        ranges = []
        if nums[0] != lower:
            ranges.append((lower, nums[0] - 1))

        for i in range(1, l):
            prev, curr = nums[i - 1], nums[i]
            if curr - 1 != prev:
                ranges.append((prev + 1, curr - 1))

        if nums[-1] != upper:
            ranges.append((nums[-1] + 1, upper))

        return ranges
