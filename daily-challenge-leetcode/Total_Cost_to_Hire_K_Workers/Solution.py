from heapq import heapify, heappop, heappush


class Solution:
    def totalCost(self, costs: list[int], k: int, cand: int) -> int:
        l, r = cand - 1, len(costs) - cand
        ans = 0
        if (cand + cand) < len(costs):
            hql = costs[: l + 1]
            hqr = costs[r:]
            heapify(hql)
            heapify(hqr)
        else:
            costs.sort()
            return sum(costs[:k])

        for _ in range(k):
            if hql and (not hqr or hql[0] <= hqr[0]):
                ans += heappop(hql)
                if l + 1 < r:
                    l += 1
                    heappush(hql, costs[l])
            elif hqr:
                ans += heappop(hqr)
                if l < r - 1:
                    r -= 1
                    heappush(hqr, costs[r])
            else:
                break
        return ans
