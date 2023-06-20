class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        ans = [-1] * min(k, length := len(nums))
        nums.append(0)
        s = sum(nums[0:k]) + sum(nums[k : k + k])
        for i in range(k, length - k):
            s += nums[i + k]
            ans.append(s // (k + 1 + k))
            s -= nums[i - k]
        ans.extend([-1] * (length - len(ans)))
        return ans
