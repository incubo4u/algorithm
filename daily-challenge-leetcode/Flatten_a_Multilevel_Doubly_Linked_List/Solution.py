# Definition for a Node.
from typing import Optional


class Node:

    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:

    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        flat = []

        def inorder(root):
            if not root:
                return
            flat.append(root)
            inorder(root.child)
            inorder(root.next)

        inorder(head)
        for i in range(1, len(flat)):
            flat[i - 1].next = flat[i]
            flat[i].prev = flat[i - 1]
            flat[i].child = None
        flat[0].child = None
        return flat[0]