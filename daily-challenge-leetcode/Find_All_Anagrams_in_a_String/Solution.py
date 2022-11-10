from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_lenght = len(p)
        s_lenght = len(s)
        chars = Counter(p)
        window = Counter()
        ans = []
        for i in range(s_lenght):
            if i < p_lenght:
                window[s[i]] += 1
            else:
                window[s[i]] += 1
                window[s[i - p_lenght]] -= 1
                if window[s[i - p_lenght]] == 0:
                    del window[s[i - p_lenght]]
            if not (chars - window):
                ans.append(i - p_lenght + 1)
        return ans
