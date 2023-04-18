from collections import deque


class Solution:

    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1, word2 = deque(word1), deque(word2)
        flip = False
        ans = []
        while word1 or word2:
            if flip and word2:
                ans.append(word2.popleft())

            if not flip and word1:
                ans.append(word1.popleft())

            flip = not flip
        return ''.join(ans)
