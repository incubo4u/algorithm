# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        def clone(root, node, seen):
            for i, n in enumerate(node.neighbors):
                if n.val not in seen:
                    seen.add(n.val)
                    root.neighbors.append(Node(n.val))
                    clone(root.neighbors[-1], n, seen)
            return root

        return clone(Node(node.val), node, set())
