# Definition for a Node.
class Node:

    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:

    def copyRandomList(self, head):
        memo = {}
        tmp = head
        while head:
            memo[head] = Node(head.val)
            head = head.next

        def deep_copy(node):
            if not node:
                return
            new_node = memo[node]
            if node.next:
                new_node.next = memo[node.next]
            if node.random:
                new_node.random = memo[node.random]
            return new_node

        head = tmp

        while head:
            new_head = deep_copy(head)
            new_head, head = new_head.next, head.next

        return memo[tmp] if tmp else None
