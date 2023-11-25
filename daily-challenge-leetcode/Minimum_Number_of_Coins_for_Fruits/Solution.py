class Solution:

    def minimumCoins(self, prices: list[int]) -> int:
        n = len(prices)

        @cache
        def buy(i, promo):
            if i > n - 1:
                return 0
            if promo:
                return min(buy(i + 1, promo - 1),
                           buy(i + 1, i + 1) + prices[i])
            return buy(i + 1, i + 1) + prices[i]

        return buy(0, 0)
