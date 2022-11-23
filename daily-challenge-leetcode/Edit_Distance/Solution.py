from functools import cache


class Solution:
    def minDistance(self, w: str, ww: str) -> int:
        l_one, l_two = len(w), len(ww)

        @cache
        def edit(o, t, cost):
            if o > l_one - 1 and t < l_two:
                return cost + len(ww) - t
            elif t > l_two - 1 and o < l_one:
                return cost + len(w) - o
            elif o > l_one - 1 and t > l_two - 1:
                return cost
            elif w[o] == ww[t]:
                return edit(o + 1, t + 1, cost)
            else:
                return min(
                    # delete
                    edit(o + 1, t, cost + 1),
                    # replace
                    edit(o + 1, t + 1, cost + 1),
                    # insert
                    edit(o, t + 1, cost + 1),
                )

        return edit(0, 0, 0)
