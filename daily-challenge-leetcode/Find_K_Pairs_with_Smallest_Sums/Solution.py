from heapq import heappop, heappush


class Solution:

    def kSmallestPairs(self, nums1: list[int], nums2: list[int],
                       k: int) -> list[list[int]]:
        hq = [(nums1[0] + nums2[0], 0, 0)]
        ans = []
        seen = set()
        while len(ans) < k and hq:
            s, o, t = heappop(hq)
            if (pair := (o, t)) in seen:
                continue
            seen.add(pair)
            ans.append((nums1[o], nums2[t]))
            if o + 1 < len(nums1):
                heappush(hq, (nums1[o + 1] + nums2[t], o + 1, t))
            if t + 1 < len(nums2):
                heappush(hq, (nums1[o] + nums2[t + 1], o, t + 1))
        return ans
