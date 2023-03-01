from typing import List


class Solution:

    def validWordSquare(self, words: List[str]) -> bool:
        padding = len(max(words, key=len))
        lenght = len(words)
        matrix = tuple(map(lambda s: s.ljust(padding, '.'), words))
        for i, w in enumerate(matrix):
            if w != ''.join(list(map(lambda j: matrix[j][i], range(lenght)))):
                return False
        return True