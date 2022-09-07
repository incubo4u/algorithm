from typing import List


class UnionFind:
    def __init__(self):
        self.groupWheight = {}

    def find(self, nodeId):
        if nodeId not in self.groupWheight:
            self.groupWheight[nodeId] = (nodeId, 1)
        groupId, nodeWheight = self.groupWheight[nodeId]
        if groupId != nodeId:
            newGroupId, groupWheight = self.find(groupId)
            self.groupWheight[nodeId] = (newGroupId, nodeWheight * groupWheight)
        return self.groupWheight[nodeId]

    def union(self, dividend, divisor, val):
        dividendGroupId, dividendWheight = self.find(dividend)
        divisorGroupId, divisorWheight = self.find(divisor)
        if dividendGroupId != divisorGroupId:
            self.groupWheight[dividendGroupId] = (
                divisorGroupId,
                divisorWheight * val / dividendWheight,
            )

    def connected(self, x, y):
        return self.find(x)[0] == self.find(y)[0]


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        u = UnionFind()
        for i, (dividend, divisor) in enumerate(equations):
            u.union(dividend, divisor, values[i])
        ret = []
        for i, (dividend, divisor) in enumerate(queries):
            if dividend not in u.groupWheight or divisor not in u.groupWheight:
                ret.append(-1)
            elif not u.connected(dividend, divisor):
                ret.append(-1)
            else:
                ret.append(u.find(dividend)[1] / u.find(divisor)[1])
        return ret
