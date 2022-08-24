import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = 1
        intervals.sort()
        heap = []
        meet = intervals.pop(0)
        heapq.heappush(heap,meet[1])
        while intervals:
            meet = intervals.pop(0)
            if heap[0] > meet[0]:
                rooms+=1
            else:
                heapq.heappop(heap)
            heapq.heappush(heap,meet[1])
            
        return rooms    
                