from heapq import heappop, heappush


class Solution:

    def largestUniqueNumber(self, nums: list[int]) -> int:
        seen = set()
        ans = []
        for n in nums:
            if -n in seen:
                continue
            elif n in seen:
                seen.add(-n)
            else:
                seen.add(n)
                heappush(ans, -n)
        while ans and ans[0] in seen:
            heappop(ans)
        return -heappop(ans) if ans else -1
