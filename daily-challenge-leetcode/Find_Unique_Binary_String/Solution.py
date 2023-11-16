class Solution:

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        nums = set(nums)
        N = len(nums) + 1
        for i in range(N):
            if (b := f"{i:0{n}b}") not in nums:
                return b
