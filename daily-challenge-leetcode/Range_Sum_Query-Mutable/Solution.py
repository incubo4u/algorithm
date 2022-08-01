
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.bitnums = [0] + nums
        self.nums = nums
        for i in range(1, len(self.bitnums)):
            ii = i + (i & -i)
            if ii < len(self.bitnums):
                self.bitnums[ii] += self.bitnums[i]

    def update(self, i: int, val: int) -> None:
        val = val - self.nums[i]
        self.nums[i]+=val
        i+=1
        while i < len(self.bitnums):
            self.bitnums[i] += val
            i += i & -i

    def sum(self, i):
        i += 1
        result = 0
        while i != 0:
            result += self.bitnums[i]
            i -= i & -i
        return result

    def sumRange(self, left: int, right: int) -> int:
        return self.sum(right) - self.sum(left-1)
