from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def getPattern(word):
            uniq = {}
            key = 0
            pattern = ""
            for i, char in enumerate(word):
                if char not in uniq:
                    uniq[char] = str(key)
                    pattern += str(key)
                    key += 1
                else:
                    pattern += uniq[char]
            return pattern

        pattern = getPattern(pattern)
        result = []
        for _, word in enumerate(words):
            if pattern == getPattern(word):
                result.append(word)
        return result
