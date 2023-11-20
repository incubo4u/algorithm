class Solution:

    def reductionOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        nums = tuple(sorted(set(nums), reverse=True))
        n = len(nums)
        ans = 0
        for i in range(1, n):
            ans += freq[nums[i - 1]]
            freq[nums[i]] += freq[nums[i - 1]]
        return ans
