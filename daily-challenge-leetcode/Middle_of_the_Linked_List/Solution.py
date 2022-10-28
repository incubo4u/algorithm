from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, node: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
