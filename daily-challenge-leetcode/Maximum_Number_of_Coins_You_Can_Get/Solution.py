class Solution:

    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()
        piles = deque(piles)
        ans = 0
        while piles:
            piles.pop()
            ans += piles.pop()
            piles.popleft()
        return ans
