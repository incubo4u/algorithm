from typing import List


class Trie:
    def __init__(self):
        self.childs = {}
        self.end = False

    def add(self, word):
        node = self
        for c in word:
            if c not in node.childs:
                node.childs[c] = Trie()
            node = node.childs[c]
        node.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        directions = [(0, +1), (+1, 0), (0, -1), (-1, 0)]
        result = []
        trie = Trie()
        path = set()

        def backtrack(x, y, word, node):
            if node.end:
                result.append(word)
                node.end = False
            if (
                x < 0
                or y < 0
                or x == len(board)
                or y == len(board[0])
                or (x, y) in path
                or board[x][y] not in node.childs
            ):
                return
            char = board[x][y]
            word += char
            path.add((x, y))
            for d in directions:
                backtrack(x + d[0], y + d[1], word, node.childs[char])
            path.remove((x, y))

        for word in words:
            trie.add(word)
        for i in range(len(board)):
            for j in range(len(board[i])):
                backtrack(i, j, "", trie)
        return result
