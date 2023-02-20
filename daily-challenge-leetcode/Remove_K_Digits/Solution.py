class Solution:

    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'
        mono = []
        for i, n in enumerate(num):
            while k and mono and mono[-1] > n:
                mono.pop()
                k -= 1
            mono.append(n)

        return str(int('0' + ''.join(mono[:len(mono) - k])))
