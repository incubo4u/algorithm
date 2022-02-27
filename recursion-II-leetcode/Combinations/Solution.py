from typing import List 
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        sub = []
        n+=1
        def comb(i,j):
            if i <= n:
                if len(sub) < k:
                    sub.append(i)
                    comb(i+1,j+1)
                    sub.pop()
                    comb(i+1,j+1)
                else: 
                    result.append(sub[:])
            
                
        comb(1,0)
        return result
s = Solution()
a = s.combine(4,2)
for i in range(len(a)):
    print(a[i])