class Node:

    def __init__(self, val, after=None, before=None):
        self.val = val
        self.next = after
        self.prev = before


class MyLinkedList:

    def __init__(self):
        self.head = self.tail = None
        self.nodes_count = 0

    def get(self, index: int, get_node=False) -> int:
        if index >= self.nodes_count:
            return -1
        ptr = self.head
        for _ in range(index):
            ptr = ptr.next
        return ptr.val if not get_node else ptr

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.tail = self.head = Node(val)
        else:
            new_head = Node(val, after=self.head)
            self.head.prev = new_head
            self.head = new_head
        self.nodes_count += 1

    def addAtTail(self, val: int) -> None:
        if not self.tail:
            self.head = self.tail = Node(val)
        else:
            new_tail = Node(val, before=self.tail)
            self.tail.next = new_tail
            self.tail = new_tail
        self.nodes_count += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.nodes_count:
            return
        elif not index:
            self.addAtHead(val)
        elif index == self.nodes_count:
            self.addAtTail(val)
        else:
            after = self.get(index, True)
            before = after.prev
            new_node = Node(val, after, before)
            after.prev = new_node
            before.next = new_node
            self.nodes_count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.nodes_count:
            return
        elif not index:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        elif index == self.nodes_count - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            rm = self.get(index, True)
            after = rm.next
            before = rm.prev
            before.next = after
            after.prev = before
        self.nodes_count -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)