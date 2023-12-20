class Solution:

    def buyChoco(self, prices: List[int], money: int) -> int:
        c = cc = inf
        for p in prices:
            if p <= cc:
                c = cc
                cc = p
            elif p <= c:
                c = p
        return money - cost if (cost := c + cc) <= money else money
