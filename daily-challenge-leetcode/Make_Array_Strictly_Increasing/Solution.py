from bisect import bisect_right
from functools import cache
from math import inf


class Solution:
    def makeArrayIncreasing(self, arr1: list[int], arr2: list[int]) -> int:
        arr2 = tuple(sorted(set(arr2)))
        l_1, l_2 = len(arr1), len(arr2)

        @cache
        def swap(prev, o):
            if o > l_1 - 1:
                return 0
            swaps = inf

            if arr1[o] > prev:
                swaps = swap(arr1[o], o + 1)

            i = bisect_right(arr2, prev)

            if i < l_2:
                swaps = min(swaps, swap(arr2[i], o + 1) + 1)

            return swaps

        return -1 if (ans := swap(-1, 0)) == inf else ans
