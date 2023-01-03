from typing import List


class Solution:

    def minDeletionSize(self, strs: List[str]) -> int:
        slen = len(strs[0])
        ans = 0
        for i in range(slen):
            l = ord('a')
            for s in strs:
                if l > ord(s[i]):
                    ans += 1
                    break
                l = ord(s[i])
        return ans
