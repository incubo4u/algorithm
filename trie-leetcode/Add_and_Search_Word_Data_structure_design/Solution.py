class WordDictionary:

    def __init__(self):
        self.childs = {}
        self.end = False

    def addWord(self, word: str) -> None:
        if len(word) == 0:
            self.end = True
            return
        c = word[0]
        if c not in self.childs:
            self.childs[c] = WordDictionary()
        self.childs[c].addWord(word[1:])
        

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self.end
        
        c = word[0]
        print(word)
        print(self.childs)
        if c == '.':
            for node in self.childs.values():
                if node.search(word[1:]):
                    return True

        if c in self.childs:
            return self.childs[c].search(word[1:])
        return False


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("dad")
obj.addWord("mad")
obj.addWord("bad")
print(obj.search("pad"))
print(obj.search("bad"))