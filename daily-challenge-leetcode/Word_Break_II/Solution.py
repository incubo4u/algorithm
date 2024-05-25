class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        del wordDict
        s_len = len(s)
        ret = []
        ans = []

        def build(w_start):
            if w_start > s_len - 1:
                ret.append(" ".join(ans))
                return

            for w_end in range(w_start, s_len):
                if (word := s[w_start:w_end + 1]) in words:
                    ans.append(word)
                    build(w_end + 1)
                    ans.pop()

        build(0)
        return ret
