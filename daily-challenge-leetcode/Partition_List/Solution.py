# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return
        left = ListNode()
        right = ListNode()
        lend = left
        rend = right

        while head:
            if head.val < x:
                lend.next = head
                lend = lend.next
            else:
                rend.next = head
                rend = rend.next
            head = head.next
        rend.next = None
        lend.next = right.next
        return left.next
