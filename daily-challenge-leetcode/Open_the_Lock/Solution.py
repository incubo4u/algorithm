class Solution:

    def openLock(self, deadends: List[str], target: str) -> int:
        target = tuple((int(n) for n in target))
        deadends = set(tuple(int(n) for n in t) for t in deadends)
        seen = set()
        que = deque([(0, 0, 0, 0, 0)])
        while que:
            (a, b, c, d, moves) = que.popleft()
            if (a, b, c, d) in deadends:
                continue
            if (a, b, c, d) in seen:
                continue
            if (a, b, c, d) == target:
                return moves

            seen.add((a, b, c, d))
            que.append(((a + 1) % 10, b, c, d, moves + 1))
            que.append((a, (b + 1) % 10, c, d, moves + 1))
            que.append((a, b, (c + 1) % 10, d, moves + 1))
            que.append((a, b, c, (d + 1) % 10, moves + 1))
            que.append((a, b - 1 * int(b - 1 >= 0) + 9 * int(b - 1 < 0), c, d,
                        moves + 1))
            que.append((a, b, c - 1 * int(c - 1 >= 0) + 9 * int(c - 1 < 0), d,
                        moves + 1))
            que.append((a - 1 * int(a - 1 >= 0) + 9 * int(a - 1 < 0), b, c, d,
                        moves + 1))
            que.append((a, b, c, d - 1 * int(d - 1 >= 0) + 9 * int(d - 1 < 0),
                        moves + 1))

        return -1
