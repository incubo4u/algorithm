from typing import Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def swapNodes(self, head: Optional[ListNode],
                  k: int) -> Optional[ListNode]:
        lenght = 0
        node = head
        while node:
            if lenght == k - 1:
                one = node
            lenght += 1
            node = node.next
        node = head
        for _ in range(lenght - k):
            node = node.next
        node.val, one.val = one.val, node.val
        return head
