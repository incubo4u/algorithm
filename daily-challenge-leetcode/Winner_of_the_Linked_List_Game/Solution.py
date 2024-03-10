# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def gameResult(self, head: Optional[ListNode]) -> str:
        even = odd = 0
        while head:
            even_wins = head.val > head.next.val
            even += int(even_wins)
            odd += int(not even_wins)
            head = head.next.next

        if even > odd:
            return "Even"
        if even < odd:
            return "Odd"
        return "Tie"
