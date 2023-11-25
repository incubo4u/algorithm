class Solution:

    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        return [i for i, s in enumerate((set(w) for w in words)) if x in s]
