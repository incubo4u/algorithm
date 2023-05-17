from collections import deque
from typing import Optional
# Definition for singly-linked list.


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def pairSum(self, node: Optional[ListNode]) -> int:
        ans, que = 0, deque()
        while node:
            que.append(node.val)
            node = node.next
        while que:
            l = que.popleft()
            ans = max(ans, l + que.pop() if que else l)
        return ans
