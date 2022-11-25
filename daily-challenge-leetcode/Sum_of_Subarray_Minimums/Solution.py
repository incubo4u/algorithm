from typing import List


class Solution:

  def sumSubarrayMins(self, nums: List[int]) -> int:
    left = []
    stack = []
    for i, n in enumerate(nums):
      prev = i
      while stack and stack[-1][1] >= n:
        prev, _ = stack.pop()
      left.append(i - prev + 1)
      stack.append((prev, n))

    right = []
    stack.clear()
    for i, n in enumerate(reversed(nums)):
      prev = i
      while stack and stack[-1][1] > n:
        prev, _ = stack.pop()
      right.append(i - prev + 1)
      stack.append((prev, n))

    mod = 10**9 + 7
    ans = 0
    for _, (l, r, n) in enumerate(zip(left, reversed(right), nums)):
      ans += l * r * n
      ans %= mod
    return ans % mod
