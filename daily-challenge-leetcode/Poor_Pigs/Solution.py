from math import ceil, log


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        T = (minutesToTest // minutesToDie) + 1
        # pigs = 0
        # while T**pigs < buckets:
        #     pigs+=1
        # return pigs
        return ceil(log(buckets, T))
