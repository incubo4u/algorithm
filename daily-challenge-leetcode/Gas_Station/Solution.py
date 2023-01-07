from typing import List


class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        gas += gas
        cost += cost
        idx = curr = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            curr += g
            curr -= c
            if curr < 0:
                idx = i + 1
                curr = 0
            if i - idx == n - 1:
                return idx
        return -1