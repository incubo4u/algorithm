from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        segment, reminder = divmod(sum(matchsticks), 4)
        if reminder != 0:
            return False
        if max(matchsticks) > segment:
            return False
        square = [0, 0, 0, 0]
        matchsticks.sort(reverse=True)

        def backtrack(i):
            if i == len(matchsticks):
                return len(set(square)) == 1
            for j in range(4):
                square[j] += matchsticks[i]
                if square[j] <= segment and backtrack(i + 1):
                    return True
                square[j] -= matchsticks[i]
                if square[j] == 0:
                    break
            return False

        return backtrack(0)
