from ast import List
from collections import Counter


class Solution:

    def uniqueOccurrences(self, arr: List[int]) -> bool:             # type: ignore
        return len(set(vals := Counter(arr).values())) == len(vals)  # type: ignore
