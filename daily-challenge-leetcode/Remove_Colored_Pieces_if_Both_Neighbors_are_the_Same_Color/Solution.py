class Solution:

    def winnerOfGame(self, colors: str) -> bool:
        a = b = bob = alice = 0
        for c in colors:
            if c == 'A':
                a += 1
                b = 0
            else:
                b += 1
                a = 0
            alice += int(a >= 3)
            bob += int(b >= 3)
        return alice > bob
