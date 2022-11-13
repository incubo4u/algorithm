class Solution:
    def maximumRemovals(self, s: str, a: str, removable):
        def contains_seq(s, a):
            ai = 0
            for c in s:
                if ai < len(a) and c == a[ai]:
                    ai += 1
                if ai == len(a):
                    return True
            return False

        def removeChars(s, indexes):
            s = list(s)
            for i, ci in enumerate(indexes):
                s[ci] = "X"
            return s

        l, r = 0, len(removable) - 1
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            if contains_seq(removeChars(s, removable[: mid + 1]), a):
                ans = mid + 1
                l = mid + 1
            else:
                r = mid - 1
        return ans
