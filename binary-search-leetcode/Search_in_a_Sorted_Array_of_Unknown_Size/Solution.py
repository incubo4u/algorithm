# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        outofbound = 2147483647
        l,r = 0,10000-1
        while l<r:
            mid = (l+r)//2
            res = reader.get(mid)
            if  res == outofbound:
                r = mid
            elif res == target:
                return mid
            elif target > res:
                l = mid+1
            else:
                r = mid
        if reader.get(l) == target:
            return l
        return -1