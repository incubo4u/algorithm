import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = 1
        intervals.sort()
        heap = []
        meeting = intervals.pop(0)
        heapq.heappush(heap,meeting[1])
        while intervals:
            meeting = intervals.pop(0)
            if heap[0] > meeting[0]:
                rooms+=1
            else:
                heapq.heappop(heap)
            heapq.heappush(heap,meeting[1])
            
        return rooms    


    # def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    #     intervals = sorted(intervals,key=lambda x: x[0])
    #     ends = sorted(intervals,key=lambda y: y[1])
    #     lenght = len(intervals)
    #     rooms=i=e=0
        
    #     while i < lenght:
    #         if intervals[i][0] >= ends[e][1]:
    #             rooms-=1
    #             e+=1
    #         rooms+=1
    #         i+=1
    #     return rooms                