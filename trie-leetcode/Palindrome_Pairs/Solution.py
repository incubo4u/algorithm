from typing import List


class Trie:
    def __init__(self):
        self.childs = {"indexes": set()}

    def add(self, word, index):
        node = self
        for _, c in enumerate(word):
            if c not in node.childs:
                node.childs[c] = Trie()
            node.childs["indexes"].add(index)
            node = node.childs[c]

    def match(self, word):
        node = self
        candidate = set()
        for i, c in enumerate(word):
            candidate = candidate.union(node.childs["indexes"])
            if c in node.childs:
                node = node.childs[c]
            else:
                break
        return candidate.union(node.childs["indexes"])


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        root = Trie()
        ret = set()
        for i, word in enumerate(words):
            root.add(word, i)

        for i, word in enumerate(words):
            candidate = root.match(word[::-1])
            for index in candidate:
                if index != i:
                    preinsert = words[index] + word
                    postinsert = word + words[index]
                    if preinsert == preinsert[::-1]:
                        ret.add((index, i))
                    if postinsert == postinsert[::-1]:
                        ret.add((i, index))
        return ret
