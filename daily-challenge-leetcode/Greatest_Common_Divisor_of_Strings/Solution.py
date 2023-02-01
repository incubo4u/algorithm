class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        tmp = str1
        while str1 and (''.join(str2.split(str1)) or ''.join(tmp.split(str1))):
            str1 = str1[:len(str1) - 1]
        return str1
