from typing import List


class TrieNode:
    def __init__(self, c):
        self.childs = {}
        self.c = c
        self.times = 0

    def add(self, s):
        self.times += 1
        if not s:
            return
        c = s[0]
        if c not in self.childs:
            self.childs[c] = TrieNode(c)
        self.childs[c].add(s[1:])

    def getPrefix(self, freq, prefix=""):
        if self.times < freq:
            return prefix
        if not self.childs or len(self.childs) > 1:
            return prefix + self.c

        child = next(iter(self.childs.keys()))
        return self.childs[child].getPrefix(freq, prefix + self.c)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = TrieNode("")
        for s in strs:
            if not s:
                return ""
            root.add(s)

        return root.getPrefix(freq=len(strs))
