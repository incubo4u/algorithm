from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = {}

        def evolveCells(cells):
            evolution = [0]
            for i in range(1, len(cells) - 1):
                evolution.append(int(cells[i - 1] == cells[i + 1]))
            evolution.append(0)
            return evolution

        while n > 0:
            key = tuple(cells)
            if key in seen:
                n %= seen[key] - n
                for _ in range(n):
                    cells = evolveCells(cells)
                break
            else:
                seen[key] = n
            if n > 0:
                n -= 1
                cells = evolveCells(cells)
        return cells
