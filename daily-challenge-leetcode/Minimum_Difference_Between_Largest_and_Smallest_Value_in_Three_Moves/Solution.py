# Runtime Percentile: 70.52120000000002
# Memory Percentile: 12.471499999999995


class Solution:

    def minDifference(self, nums: List[int]) -> int:
        if (n := len(nums)) <= 4:
            return 0
        ans = 0
        nums.sort()

        def get_min(l, r, step):
            if not step:
                return nums[r] - nums[l]

            return min(
                get_min(l + 1, r, step - 1),
                get_min(l, r - 1, step - 1),
                nums[r] - nums[l],
            )

        return get_min(0, n - 1, 3)
