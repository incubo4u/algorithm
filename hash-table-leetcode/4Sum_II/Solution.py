from typing import List


class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:

        firstmemo = {}
        secondmemo = {}
        for n in nums1:
            for nn in nums2:
                s = n + nn
                if s not in firstmemo:
                    firstmemo[s] = 1
                else:
                    firstmemo[s] += 1

        for n in nums3:
            for nn in nums4:
                s = n + nn
                if -(s) not in firstmemo:
                    continue
                elif s not in secondmemo:
                    secondmemo[s] = 1
                else:
                    secondmemo[s] += 1
        comb = 0
        for key in secondmemo:
            comb += secondmemo[key]*firstmemo[-(key)]
        return comb