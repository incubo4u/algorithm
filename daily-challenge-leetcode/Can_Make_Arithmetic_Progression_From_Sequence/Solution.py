from collections import defaultdict


class Solution:

    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        count = defaultdict(int)
        o = t = 1000000
        if len(arr) < 3:
            return True

        for n in arr:
            if o >= n:
                t = o
                o = n
            elif t > n:
                t = n
            count[n] += 1

        d = t - o
        if not d:
            return len(set(arr)) == 1

        for n in arr:
            if n == o:
                continue
            m = n - d
            if not count[m]:
                return
            count[m] -= 1
            if not count[m]:
                del count[m]
        return True
