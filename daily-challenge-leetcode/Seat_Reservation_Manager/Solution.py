from heapq import heappop, heappush


class SeatManager:

    def __init__(self, n: int):
        self.free = list(range(1, n + 1))

    def reserve(self) -> int:
        return heappop(self.free)

    def unreserve(self, seat: int) -> None:
        heappush(self.free, seat)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
