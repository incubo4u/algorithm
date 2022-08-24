from math import sqrt
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return [
            pd[1] for pd in 
            sorted(list(map(lambda p: (sqrt(p[0]**2+p[1]**2),(p[0],p[1])) ,points)),key=lambda dp: dp[0])[:k]
            ]
        
                    
                
                    