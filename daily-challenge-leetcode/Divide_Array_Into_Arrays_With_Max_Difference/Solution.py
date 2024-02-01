class Solution:

    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(2, n, 3):
            if nums[i] - nums[i - 2] > k:
                return []
            ans.append(nums[i - 2:i + 1])
        return ans
