class Solution:

    def countNicePairs(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        count = defaultdict(list)
        ans = 0
        for i, n in enumerate(nums):
            key = n - int(str(n)[::-1])
            ans += len(count[key])
            count[key].append(i)
        return ans % mod
