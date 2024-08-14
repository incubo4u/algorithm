# Runtime Percentile: 5.0412000000001935
# Memory Percentile: 5.020200000000006


class Solution:

    def numberOfPatterns(self, m: int, n: int) -> int:
        move_by_one = (
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (2, 1),
            (2, -1),
            (-2, -1),
            (-2, 1),
            (-1, -2),
            (1, -2),
            (-1, 2),
            (1, 2),
        )
        move_by_two = (
            (0, 2),
            (0, -2),
            (2, 0),
            (-2, 0),
            (-2, -2),
            (2, 2),
            (2, -2),
            (-2, 2),
        )

        @cache
        def to_by_one_move(x):
            remove = 0
            if x < 0:
                remove = +1
            elif x > 0:
                remove = -1
            return x + remove

        @cache
        def unlock(moves):
            i, j = moves[-1]

            if m <= len(moves) <= n:
                nonlocal ans
                ans += 1

            if len(moves) > n:
                return

            for y, x in move_by_one:
                if (0 <= (yi := y + i) < 3 and 0 <= (xj := x + j) < 3
                        and (yi, xj) not in moves):
                    unlock((*moves, (yi, xj)))

            for y, x in move_by_two:
                if (0 <= (yi := to_by_one_move(y) + i) < 3 and 0 <=
                    (xj := to_by_one_move(x) + j) < 3 and (yi, xj) in moves
                        and 0 <= (yi := y + i) < 3 and 0 <= (xj := x + j) < 3
                        and (yi, xj) not in moves):
                    unlock((*moves, (yi, xj)))

        ans = 0
        for i, j in product(range(3), range(3)):
            unlock(((i, j), ))
        return ans
