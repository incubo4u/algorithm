class Solution:
    def concatenatedBinary(self, n: int) -> int:
        return int("".join(bin(i)[2:] for i in range(n+1) ),2)%((10**9)+7)