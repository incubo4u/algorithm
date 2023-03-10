from random import randint
from typing import Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.lenght = 0
        self.setLenght(head)

    def setLenght(self, head):
        while head.next:
            self.lenght += 1
            head = head.next

    def getRandom(self) -> int:
        r = randint(0, self.lenght)
        node = self.head
        while r:
            r -= 1
            node = node.next
        return node.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()