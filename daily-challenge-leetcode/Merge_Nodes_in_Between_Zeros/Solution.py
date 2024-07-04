# Runtime Percentile: 81.95479999999975
# Memory Percentile: 62.963100000000004


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        end = start.next
        curr_sum = 0

        while end:
            while end.val:
                curr_sum += end.val
                end = end.next

            start.val = curr_sum
            curr_sum = 0
            start.next = end
            if end.next:
                start = start.next
            else:
                start.next = None
            end = end.next
        return head
