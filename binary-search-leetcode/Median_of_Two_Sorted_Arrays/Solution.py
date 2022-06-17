import sys
from typing import List


class Solution:
    def findMedianSortedArrays(self, fist: List[int], second: List[int]) -> float:
        if len(second) < len(fist):
            fist, second = second, fist
        lenght = len(fist) + len(second)
        half = lenght // 2
        even = lenght % 2 == 0
        l, r = 0, len(fist) - 1
        while True:
            borderFirst = (l + r) // 2
            borderSecond = half - borderFirst - 2
            
            lastLeftValueFirst = fist[borderFirst] if borderFirst >= 0 else -sys.maxsize
            lastLeftValueSecond = second[borderSecond] if borderSecond >= 0 else -sys.maxsize
            rightOne = fist[borderFirst + 1] if borderFirst + 1 < len(fist) else sys.maxsize
            rightTwo = second[borderSecond + 1] if borderSecond + 1 < len(second) else sys.maxsize
            
            if lastLeftValueFirst <= rightTwo and lastLeftValueSecond <= rightOne:
                break
            elif lastLeftValueFirst > rightTwo:
                r = borderFirst - 1
            else:
                l = borderFirst + 1
        if even:
            return (max(lastLeftValueFirst, lastLeftValueSecond) + min(rightOne, rightTwo)) / 2
        else:
            return min(rightOne, rightTwo)

