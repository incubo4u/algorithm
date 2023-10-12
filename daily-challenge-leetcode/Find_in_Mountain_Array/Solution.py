# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

from collections import defaultdict
from math import inf


class Solution:

    def findInMountainArray(self, target: int, ARR: 'MountainArray') -> int:
        n = ARR.length()
        l, r = 0, n - 1
        seen_values = {}
        minimum_index = defaultdict(lambda: inf)

        while l < r:

            m = (l + r) // 2

            left = ARR.get(l)
            seen_values[l] = left
            minimum_index[left] = min(minimum_index[left], l)

            right = ARR.get(r)
            seen_values[r] = right
            minimum_index[right] = min(minimum_index[right], r)

            mid = ARR.get(m)
            seen_values[m] = mid
            minimum_index[mid] = min(minimum_index[mid], m)

            if left < mid and left <= right:
                l = m
            else:
                r = m

        ll, rr = l + 1, n - 1
        l, r = 0, l

        while l < r:
            m = (l + r) // 2
            curr = seen_values.get(m, ARR.get(m))
            minimum_index[curr] = min(minimum_index[curr], m)

            if curr > target:
                r = m
            else:
                l = m + 1

        while ll < rr:
            m = (ll + rr) // 2
            curr = seen_values.get(m, ARR.get(m))
            minimum_index[curr] = min(minimum_index[curr], m)
            if curr > target:
                ll = m + 1
            else:
                rr = m

        return minimum_index[target] if minimum_index[target] != inf else -1
