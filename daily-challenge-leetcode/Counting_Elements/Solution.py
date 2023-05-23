from collections import Counter


class Solution:
    def countElements(self, arr: list[int]) -> int:
        arr = Counter(arr)
        return sum(arr[n] for n in arr if n + 1 in arr)
