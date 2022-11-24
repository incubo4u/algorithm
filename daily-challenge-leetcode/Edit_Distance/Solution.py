from functools import cache


class Solution:
    def minDistance(self, word_one: str, word_two: str) -> int:
        l_one, l_two = len(word_one), len(word_two)

        @cache
        def edit(o, t, cost):
            if o > l_one - 1 and t < l_two:
                return cost + l_two - t
            elif t > l_two - 1 and o < l_one:
                return cost + l_one - o
            elif o > l_one - 1 and t > l_two - 1:
                return cost
            elif word_one[o] == word_two[t]:
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
