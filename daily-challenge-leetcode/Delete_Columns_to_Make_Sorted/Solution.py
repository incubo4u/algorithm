from typing import List


class Solution:

    def minDeletionSize(self, strs: List[str]) -> int:
        lenght = len(strs[0])
        ans = 0
        for i in range(lenght):
            o = ord('a')
            for s in strs:
                if o > ord(s[i]):
                    ans += 1
                    break
                o = ord(s[i])
        return ans
