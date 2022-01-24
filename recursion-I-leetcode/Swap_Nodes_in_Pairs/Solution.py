# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        if head.next is None:
            return head
        first = head
        second = head.next
        nextPair = head.next.next

        second.next = first
        first.next = self.swapPairs(nextPair)
        return second 