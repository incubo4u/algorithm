from typing import List


class Solution:

    def minimumHealth(self, damage: List[int], armor: int) -> int:
        damage.sort()
        return 1 + max(0, damage.pop() - armor) + sum(damage)
