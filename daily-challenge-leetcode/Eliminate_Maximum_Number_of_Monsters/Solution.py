class Solution:

    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = 1
        hq = [ceil(d / s) for _, (d, s) in enumerate(zip(dist, speed))]
        heapify(hq)
        heappop(hq)
        while hq:
            monster = heappop(hq)
            if monster > time:
                time += 1
            else:
                return time
        return time
