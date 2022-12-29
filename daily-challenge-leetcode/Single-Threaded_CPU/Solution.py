from heapq import heappop, heappush


class Solution:

    def getOrder(self, T):
        T = list(map(lambda t: (t[1][0], t[1][1], t[0]), enumerate(T)))
        T.sort(key=lambda t: (-t[0], -t[1], -t[2]))
        curr, cost, i = T.pop()
        pending = [(cost, i)]
        ans = []
        while pending:
            cost, i = heappop(pending)
            ans.append(i)
            curr += cost
            while T and curr >= T[-1][0]:
                _, cost, i = T.pop()
                heappush(pending, (cost, i))
            if not pending and T:
                curr, cost, i = T.pop()
                heappush(pending, (cost, i))
        return ans