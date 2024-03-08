# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def frequenciesOfElements(self,
                              head: Optional[ListNode]) -> Optional[ListNode]:
        counter = defaultdict(int)
        while head:
            counter[head.val] += 1
            head = head.next
        node = ListNode(0)
        head = node
        n = len(counter)
        for i, (_, freq) in enumerate(counter.items()):
            node.val = freq
            if i != n - 1:
                node.next = ListNode(0)
                node = node.next
        return head
