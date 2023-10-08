class Trie:

    def __init__(self):
        self.end = self.count = 0
        self.childs = {}

    def insert(self, s: str, operation=1) -> None:
        self.count += operation
        if not s:
            self.end += operation
            return
        c = s[0]
        if c not in self.childs:
            self.childs[c] = Trie()
        self.childs[c].insert(s[1:], operation)

    def erase(self, s: str) -> None:
        self.insert(s, -1)

    def countWordsEqualTo(self, s: str, use_end=1) -> int:
        if not s: return self.end * use_end + self.count * int(not use_end)
        c = s[0]
        if c not in self.childs: return 0
        return self.childs[c].countWordsEqualTo(s[1:], use_end)

    def countWordsStartingWith(self, prefix: str) -> int:
        return self.countWordsEqualTo(prefix, 0)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)n
