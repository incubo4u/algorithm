from bisect import bisect_left, bisect_right


class Solution:

    def fullBloomFlowers(self, flowers: list[list[int]], people: list[int]):
        starts, ends = zip(*flowers)
        starts, ends = list(starts), list(ends)
        starts.sort(), ends.sort()
        return (bisect_right(starts, p) - bisect_left(ends, p) for p in people)
