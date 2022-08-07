class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a, e, i, o, u = 1, 1, 1, 1, 1
        n -= 1
        while n > 0:
            n -= 1
            newA = e + i + u
            newE = a + i
            newI = a + e + o + u
            newO = i + u
            newU = a
            a = newA
            e = newE
            i = newI
            o = newO
            u = newU

        return (a + e + i + o + u) % 1000000007
