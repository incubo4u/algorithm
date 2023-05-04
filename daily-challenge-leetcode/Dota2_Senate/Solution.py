from collections import deque


class Solution:

    def predictPartyVictory(self, senate: str) -> str:
        rounds = deque(senate)
        r = d = 0
        seenR = seenD = True
        while (lenght := len(rounds)) > 1 and seenR and seenD:
            seenR = seenD = False
            for _ in range(lenght):
                senator = rounds.popleft()
                if r > 0 and senator == 'D':
                    r -= 1
                    continue
                elif d > 0 and senator == 'R':
                    d -= 1
                    continue

                if senator == 'R':
                    r += 1
                    seenR = True
                elif senator == 'D':
                    d += 1
                    seenD = True
                rounds.append(senator)
        return 'Radiant' if rounds.popleft() == 'R' else 'Dire'