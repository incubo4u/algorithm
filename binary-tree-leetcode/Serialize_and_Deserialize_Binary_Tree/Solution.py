# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


class Codec:
    def serialize(self, root):
        if not root:
            return ""
        binstr = ""
        que = []
        que.append(root)
        while len(que) > 0:
            floor = []
            lenght = len(que)
            for i in range(lenght):
                node = que.pop(0)
                if node:
                    binstr += str(node.val)
                    que.append(node.left)
                    que.append(node.right)
                else:
                    binstr += "n"
                binstr += ","
        return binstr[:-1]

    def deserialize(self, data):
        if len(data) == 0:
            return
        data = data.split(",")
        root = TreeNode(int(data.pop(0)))
        que = []
        que.append(root)
        while len(que) > 0 and len(data) > 0:
            lenght = len(que)
            for i in range(lenght):
                node = que.pop(0)
                if node:
                    leftValue = data.pop(0)
                    rightValue = data.pop(0)
                    if leftValue != "n":
                        node.left = TreeNode(int(leftValue))
                        que.append(node.left)
                    if rightValue != "n":
                        node.right = TreeNode(int(rightValue))
                        que.append(node.right)
        return root
