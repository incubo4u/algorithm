from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}
        for num in nums1:
            if num in count:
                count[num][0] += 1
            else:
                count[num] = [1, 0]
        if len(count) < 0:
            return []
        for num in nums2:
            if num in count:
                count[num][1] += 1
        result = []
        for num in count.keys():
            times = min(count[num][0], count[num][1])
            for i in range(times):
                result.append(num)
        return result

