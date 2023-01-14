class Solution:

    def countBits(self, n: int):

        def count(x):
            count = 0
            while x:
                count += 1
                x &= x - 1
            return count

        return (count(i) for i in range(n + 1))
