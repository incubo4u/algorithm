# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def plusOne(self, head: ListNode) -> ListNode:

        def addOne(head):
            if not head:
                return 1
            head.val += addOne(head.next)
            if head.val > 9:
                head.val = 0
                return 1
            return 0

        if addOne(head):
            return ListNode(1, head)
        return head
