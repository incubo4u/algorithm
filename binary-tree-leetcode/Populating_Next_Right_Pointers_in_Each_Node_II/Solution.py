# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return
        queue = [] 
        queue.append(root)
        while len(queue) > 0:
            floor = []
            lenght = len(queue)
            for i in range(lenght):
                node = queue.pop(0)
                if node:
                    floor.append(node)
                    queue.append(node.left)
                    queue.append(node.right)
                if len(floor) > 1:
                    for i in range(1,len(floor)):
                        floor[i-1].next = floor[i]
        return root
