class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # return len(set(zip(s, t))) == len(set(s)) == len(set(t))
        def getPattern(word):
            uniq = {}
            key = 0
            pattern = []
            for i, char in enumerate(word):
                if char not in uniq:
                    uniq[char] = str(key)
                    pattern.append(str(key))
                    key+=1
                else:
                    pattern.append(uniq[char])
            return pattern
        return getPattern(s) == getPattern(t)
