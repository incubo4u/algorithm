class MapSum:
    def __init__(self):
        self.childs = {}
        self.value = 0
        self.end = False

    def insert(self, key: str, val: int) -> None:
        if len(key) == 0:
            self.value = val
            self.end = True
            return
        c = key[0]
        if c not in self.childs:
            self.childs[c] = MapSum()
        self.childs[c].insert(key[1:], val)

    def dfs(self, root):
        sum = 0
        if root.end == True:
            sum += root.value
        for node in root.childs.values():
            sum += self.dfs(node)
        return sum

    def sum(self, prefix: str) -> int:
        if len(prefix) == 0:
            return self.dfs(self)
        c = prefix[0]
        if c in self.childs:
            return self.childs[c].sum(prefix[1:])
        return 0