class Trie:
    def __init__(self):
        self.childs = {}
        self.end = False

    def insert(self, word: str) -> None:
        if len(word) == 0:
            self.end = True
            return
        c = word[0]
        if c not in self.childs:
            self.childs[c] = Trie()
        self.childs[c].insert(word[1:])

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self.end
        c = word[0]
        if c in self.childs:
            return self.childs[c].search(word[1:])
        return False

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True
        c = prefix[0]
        if c in self.childs:
            return self.childs[c].startsWith(prefix[1:])
        return False
