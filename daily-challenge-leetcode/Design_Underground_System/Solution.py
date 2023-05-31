from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.duration = defaultdict(list)
        self.check_in = defaultdict(tuple)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        f, s = self.check_in[id]
        self.duration[(f, stationName)].append(t - s)

    def getAverageTime(self, f: str, to: str) -> float:
        return sum(self.duration[(f, to)]) / len(self.duration[(f, to)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
