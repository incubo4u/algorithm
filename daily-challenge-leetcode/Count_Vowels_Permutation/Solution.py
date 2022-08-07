class Solution:
    def countVowelPermutation(self, n: int) -> int:
        vowel = [[1, 1, 1, 1, 1]]
        n -= 1
        while n > 0:
            last = vowel[-1]
            a = last[1] + last[2] + last[4]
            e = last[0] + last[2]
            i = last[1] + last[3]
            o = last[2]
            u = last[2] + last[3]
            vowel.append([a, e, i, o, u])
            n -= 1
        result = sum(vowel[-1])
        return result % (pow(10, 9) + 7)
