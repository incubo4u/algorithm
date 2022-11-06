from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ret = []
        curr = ""
        for i, c in enumerate(s, 1):
            if i % k == 0:
                ret.append(curr + c)
                curr = ""
            else:
                curr += c
        if curr:
            ret.append(curr + fill * (k - len(curr)))
        return ret
