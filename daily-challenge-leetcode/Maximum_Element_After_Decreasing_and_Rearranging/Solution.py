class Solution:

    def maximumElementAfterDecrementingAndRearranging(self,
                                                      arr: List[int]) -> int:
        n = len(arr)
        ans = 1
        arr.sort()
        for i in range(1, n):
            if arr[i] >= ans + 1:
                ans += 1
        return ans
