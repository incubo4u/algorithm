# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Codec:
    def serialize(self, root: "Node") -> str:
        if not root:
            return ""
        serialized = f"{root.val}n"
        que = [root]
        while que:
            root = que.pop(0)
            if root:
                que.extend(root.children)
                for i, node in enumerate(root.children):
                    serialized += f"{node.val}"
                    if i != len(root.children) - 1:
                        serialized += ","
                serialized += "n"
        return serialized

    def deserialize(self, data: str) -> "Node":
        if len(data) == 0:
            return
        tree = list(map(lambda x: x.split(","), data.split("n")))
        if tree[0][0] != "":
            root = Node(int(tree.pop(0)[0]), [])
        que = [root]
        while que:
            node = que.pop(0)
            level = tree.pop(0)
            for elm in level:
                if elm != "":
                    child = Node(int(elm), [])
                    node.children.append(child)
                    que.append(child)
        return root
