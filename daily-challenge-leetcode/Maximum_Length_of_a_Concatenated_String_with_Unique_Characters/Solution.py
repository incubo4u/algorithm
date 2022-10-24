from functools import cache


class Solution:
    def maxLength(self, arr) -> int:
        lenght = len(arr)

        @cache
        def get_max(i, best):
            if i > lenght - 1:
                return len(best)
            curr, scurr = arr[i], set(arr[i])
            if len(curr) != len(scurr):
                return get_max(i + 1, best)
            elif not set(best).intersection(scurr):
                return max(get_max(i + 1, best + curr), get_max(i + 1, best))
            else:
                return get_max(i + 1, best)

        return get_max(0, "")
