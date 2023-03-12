from typing import Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return
        node = head
        n = 0
        while node:
            n += 1
            node = node.next

        def build(n):
            if n:
                left = build(int(n / 2))
                nonlocal head
                root = head
                head = head.next
                root.left = left
                root.right = build(int(n - int(n / 2) - 1))
                return root

        return build(n)

        # vals = []
        # while head:
        #     vals.append(head)
        #     head = head.next
        # n = len(vals)

        # def build(l, r):
        #     if l > r:
        #         return
        #     m = (l + r) // 2
        #     root = TreeNode(vals[m].val)
        #     if l == r:
        #         return root
        #     root.left = build(l, m - 1)
        #     root.right = build(m + 1, r)
        #     return root

        # return build(0, n - 1)
