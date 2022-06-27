from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def divideNotExceeding(limit):
            largestSum = 0
            currentSum = 0
            cut = m - 1
            for elm in nums:
                if cut < 0:
                    return -1
                if currentSum + elm <= limit:
                    currentSum += elm
                else:
                    cut -= 1
                    currentSum = elm
                largestSum = max(currentSum, largestSum)
            # True or False  could be returned instead
            if cut > 0:
                return largestSum
            elif cut == 0:
                return 0
            else:
                return -1

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            result = divideNotExceeding(mid)
            if result > 0:
                right = result
            elif result == 0:
                right = mid
            else:
                left = mid + 1
        return left
