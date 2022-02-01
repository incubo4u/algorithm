from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        j = 0
        z = s.copy()
        for i in reversed(z):
            s[j] = i
            j+=1