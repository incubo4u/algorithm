from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words.sort()
        wordLenght = len(words[0])
        lenght = len(words) * wordLenght
        ret = []
        for i in range(len(s) - (lenght - 1)):
            window = s[i : i + lenght]
            currentWords = sorted(
                [window[j : j + wordLenght] for j in range(0, len(window), wordLenght)]
            )
            if currentWords == words:
                ret.append(i)
        return ret
