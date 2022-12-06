# Definition for singly-linked list.
from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        j, end = 1, head
        while end.next:
            end = end.next
            j += 1
        i, node = 1, head
        while i < j:
            if i % 2 == 1:
                end.next = ListNode(node.next.val)
                end, node.next = end.next, node.next.next
                i += 1
            node = node.next
            i += 1
        return head
