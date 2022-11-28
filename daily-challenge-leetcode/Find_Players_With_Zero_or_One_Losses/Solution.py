from collections import Counter


class Solution:

    def findWinners(self, matches):
        counters = map(Counter, zip(*matches))
        winers = next(iter(counters))
        losers = []
        for _, (loser, times) in enumerate(next(iter(counters)).items()):
            del winers[loser]
            if times < 2:
                losers.append(loser)
        return (sorted(winers.keys()), sorted(losers))
