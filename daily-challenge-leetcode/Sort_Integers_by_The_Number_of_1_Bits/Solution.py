class Solution:

    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda i: (i.bit_count(), i))
        return arr
