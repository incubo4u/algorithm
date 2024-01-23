class Solution:
    def maxLength(self, arr: list[str]) -> int:
        n = len(arr)
        def connect(i,seen):
            if i > n-1:
                return 0
            ans = connect(i+1,seen)
            for c in arr[i]:
                idx = ord(c) - ord('a')
                if (seen >> idx ) & 1:
                    return ans 
                seen ^= 1 << idx
            return max(connect(i+1,seen) + len(arr[i]),ans)
        return connect(0,0)

            
            

