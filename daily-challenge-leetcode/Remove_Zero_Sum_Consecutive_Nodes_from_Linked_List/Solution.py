# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def removeZeroSumSublists(self,
                              head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        start = dummy
        curr_sum = 0
        seen = {}
        while start:
            curr_sum += start.val
            seen[curr_sum] = start
            start = start.next
        start = dummy
        curr_sum = 0
        while start:
            curr_sum += start.val
            if curr_sum in seen:
                start.next = seen[curr_sum].next
            start = start.next
        return dummy.next
