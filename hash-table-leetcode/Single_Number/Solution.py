from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # return Counter(nums).most_common()[-1][0]
        s= set()
        for _,nr in enumerate(nums):
            if nr not in s:
                s.add(nr)
            else:
                s.remove(nr)
        return list(s)[0]
        