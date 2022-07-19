from typing import List


class Solution:
    def __init__(self):
        self.childs = {}
        self.end = False

    def matchMinPrefix(self, word, depth):
        if self.end:
            return depth
        if len(word) == 0:
            return 0
        c = word[0]
        if c in self.childs:
            return self.childs[c].matchMinPrefix(word[1:], depth + 1)
        return 0

    def insert(self, val):
        if len(val) == 0:
            self.end = True
            return
        c = val[0]
        if c not in self.childs:
            self.childs[c] = Solution()
        self.childs[c].insert(val[1:])

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        while len(dictionary) > 0:
            self.insert(dictionary.pop())
        sentence = sentence.split(" ")
        for i, word in enumerate(sentence):
            cut = self.matchMinPrefix(word, 0)
            if cut > 0:
                sentence[i] = word[:cut]
        return " ".join(sentence)
