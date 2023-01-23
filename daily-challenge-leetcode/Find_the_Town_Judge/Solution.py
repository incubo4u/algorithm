from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        '''
        If the town judge exists, then:
            The town judge trusts nobody.
            Everybody (except for the town judge) trusts the town judge.
        '''
        trusted = [0]*n
        trusting = [0]*n
        for a,b in trust:
            trusted[b-1] +=1
            trusting[a-1] += 1
        for i ,(ind ,outd) in enumerate(zip(trusted,trusting)):
            if ind == n-1 and not outd:
                return i+1
        return -1
            