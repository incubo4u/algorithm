class Solution:

    def maxScoreWords(self, words: List[str], letters: List[str],
                      score: List[int]) -> int:
        freq = Counter(letters)
        word_score = Counter()
        for w in words:
            if w in word_score:
                continue
            for c in w:
                i = ord(c) - ord("a")
                word_score[w] += score[i]

        def backtrack(i):
            if i > len(words) - 1:
                return 0
            nonlocal freq
            wc = Counter(words[i])
            missing_c = wc - freq
            best = backtrack(i + 1)
            if not missing_c:
                freq -= wc
                best = max(best, backtrack(i + 1) + word_score[words[i]])
                freq += wc
            return best

        return backtrack(0)
