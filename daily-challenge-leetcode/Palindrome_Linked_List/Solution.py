from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        if not head.next.next:
            return head.val == head.next.val

        def findMid(head):
            slow = fast = head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            return slow

        mid = findMid(head)

        curr = mid.next
        prev = None
        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after

        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
