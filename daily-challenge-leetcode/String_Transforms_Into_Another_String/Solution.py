from collections import defaultdict


class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        g = defaultdict(set)
        seen_letters = set()
        for one, two in zip(str1, str2):
            g[one].add(two)
            seen_letters.add(two)
            if len(g[one]) > 1:
                return False
        if len(seen_letters) < 26:
            return True
        return False
