from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return max(nums)

        curr, neighbour, next_neighbour = 0, nums[n - 1], 0
        ans = 0
        for i in range(n - 2, -1, -1):
            if i == 0:
                break
            curr, next_neighbour = max(neighbour, next_neighbour + nums[i]), neighbour
            neighbour = curr
        ans = max(ans, curr)

        curr, neighbour, next_neighbour = 0, nums[n - 2], 0
        for i in range(n - 3, -1, -1):
            curr, next_neighbour = max(neighbour, next_neighbour + nums[i]), neighbour
            neighbour = curr
        ans = max(ans, curr)

        return ans
