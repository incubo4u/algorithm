from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [nr[0] for nr in Counter(nums).most_common()[:k]]
        