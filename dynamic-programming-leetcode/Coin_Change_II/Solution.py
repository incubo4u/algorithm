from functools import cache
from typing import List


class Solution:

    def change(self, amount: int, coins: List[int]) -> int:

        @cache
        def get_ways(i, amt):
            if amt > amount or i > len(coins) - 1:
                return 0
            elif amt == amount:
                return 1
            else:
                return get_ways(i, amt + coins[i]) + get_ways(i + 1, amt)

        return get_ways(0, 0)
