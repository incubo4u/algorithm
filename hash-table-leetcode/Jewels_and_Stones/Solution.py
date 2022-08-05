from collections import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = Counter(stones)
        return sum(map(lambda x , counter=counter: counter.get(x,0),jewels))
        