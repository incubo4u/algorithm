from collections import Counter
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        halfLenght = len(arr) // 2
        counter = Counter(arr).most_common()
        if len(counter) == 1:
            return 1
        for i, (_, amount) in enumerate(counter):
            if halfLenght > 0:
                halfLenght -= amount
            else:
                return i
