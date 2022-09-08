from bisect import bisect


class HitCounter:
    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
            return bisect(self.hits, timestamp) - bisect(self.hits, timestamp - 300)