# Runtime Percentile: 58.42690000000009
# Memory Percentile: 29.213400000000007


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def nodesBetweenCriticalPoints(self,
                                   head: Optional[ListNode]) -> List[int]:
        l, m = head, head.next
        if not m.next: return [-1, -1]
        min_d, max_d = inf, -inf
        i = prev = 0
        first = -1
        r = m.next
        while r:
            if l.val < m.val > r.val or l.val > m.val < r.val:
                if first == -1:
                    prev = first = i
                else:
                    min_d = min(i - prev, min_d)
                    max_d = i - first
                    prev = i
            i += 1
            r = r.next
            m = m.next
            l = l.next
        if inf == min_d:
            return [-1, -1]
        return [min_d, max_d]
