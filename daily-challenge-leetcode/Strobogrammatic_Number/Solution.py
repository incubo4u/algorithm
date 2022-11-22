from collections import deque


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strobo = deque()
        for i,n in enumerate(num):
            if n == '6':
                strobo.appendleft('9')
            elif n == '9':
                strobo.appendleft('6')
            elif n not in ('8','0','1'):
                return False      # ^ (╯°□°）╯︵ ┻━┻
            else:
                strobo.appendleft(n)
        return "".join(strobo) == num
                
                
            
        
                
        