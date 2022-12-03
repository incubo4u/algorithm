class Solution:

    def kidsWithCandies(self, candies, extraCandies):
        greatest = max(candies) - extraCandies
        return map(lambda c: c >= greatest, candies)
