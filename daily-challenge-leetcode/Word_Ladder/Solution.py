class Solution:

    def ladderLength(self, start: str, end: str, w: list[str]) -> int:
        n = len(w)
        que = deque([(start, 1)])
        w = set(w + [start])
        if end not in w:
            return 0
        while que:
            curr, dist = que.popleft()
            if curr not in w:
                continue
            w.remove(curr)
            for i in range(len(curr)):
                for c in string.ascii_lowercase:
                    new_curr = curr[:i] + c + curr[i + 1:]
                    if new_curr == end:
                        return dist + 1
                    if new_curr in w:
                        que.append((new_curr, dist + 1))
        return 0
