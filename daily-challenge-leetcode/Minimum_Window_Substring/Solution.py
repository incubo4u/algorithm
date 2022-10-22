from collections import Counter, deque


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needed = Counter(t)
        seen = deque()
        ans = ""
        for i, c in enumerate(s):
            if c not in needed:
                continue
            seen.append((i, c))
            needed[c] -= 1
            if max(needed.values()) <= 0:
                while needed[seen[0][1]] < 0:
                    dc = seen.popleft()
                    needed[dc] += 1
                if not ans:
                    ans = s[seen[0][0] : i + 1]
                ans = min(ans, s[seen[0][0] : i + 1], key=len)
                dc = seen.popleft()
                needed[dc] += 1
        return ans
