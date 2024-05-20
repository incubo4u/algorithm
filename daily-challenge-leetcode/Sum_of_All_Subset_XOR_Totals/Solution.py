class Solution:

    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        nr = reduce(lambda a, b: a | b, nums)
        freq = 1 << n - 1
        return sum(bool(nr & (1 << i)) * ((1 << i) * freq) for i in range(n))
