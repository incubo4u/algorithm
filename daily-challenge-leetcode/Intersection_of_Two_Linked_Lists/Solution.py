from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, A: ListNode, B: ListNode) -> Optional[ListNode]:
        seen = set()
        while A:
            seen.add(A)
            A = A.next
        while B:
            if B in seen:
                return B
            B = B.next
        