class Solution:
    def calculateTime(self, keyboard: str, w: str) -> int:
        d = { val:idx  for idx , val in enumerate(keyboard) }
        ans = 0 
        curr = 0 
        for c in  w:
            ans += abs(curr - d[c]) 
            curr = d[c]
        return ans 
        