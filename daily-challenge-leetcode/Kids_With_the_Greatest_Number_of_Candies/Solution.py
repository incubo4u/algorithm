class Solution:

    def kidsWithCandies(self, candies, extraCandies):
        greatest = max(candies)
        return map(lambda c: c + extraCandies >= greatest, candies)
