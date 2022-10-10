from collections import defaultdict
from sortedcontainers import SortedList


class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MaxStack:
    def __init__(self):
        self.nodes = defaultdict(list)
        self.sorted_nodes = SortedList()
        self.root = Node()
        self.last = None

    def push(self, x: int) -> None:
        node = Node(x)
        self.sorted_nodes.add(node.val)
        self.nodes[node.val].append(node)
        if not self.last:
            self.last = node
            self.root.next = self.last
            self.last.prev = self.root
        else:
            self.last.next = node
            node.prev = self.last
            self.last = self.last.next

    def pop(self) -> int:
        ret = self.last.val
        self.last = self.last.prev
        self.last.next = None
        self.nodes[ret].pop()
        self.sorted_nodes.remove(ret)
        return ret

    def top(self) -> int:
        return self.last.val

    def peekMax(self) -> int:
        return self.sorted_nodes[-1]

    def popMax(self) -> int:
        if self.last.val == self.peekMax():
            return self.pop()
        ret = self.sorted_nodes.pop()
        to_remove = self.nodes[ret].pop()
        p = to_remove.prev
        n = to_remove.next
        p.next = n
        n.prev = p
        return ret
