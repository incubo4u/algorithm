class Solution:

    def confusingNumber(self, n: int) -> bool:
        d = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        s = str(n)
        r = []
        for digit in s:
            if digit in d:
                r.append(d[digit])
            else:
                return False
        return ''.join(r[::-1]) != s
