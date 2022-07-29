from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        keys = map(tuple,map(sorted,strs))
        for i , key in enumerate(keys):
            if key in h:
                h[key].append(strs[i])
            else:
                h[key] = [strs[i]]
        return h.values()