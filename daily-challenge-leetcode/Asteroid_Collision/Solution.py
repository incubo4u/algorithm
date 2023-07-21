class Solution:

    def asteroidCollision(self, rocks: List[int]) -> List[int]:
        n = len(rocks)
        s = []
        for r in rocks:
            if not s:
                s.append(r)
            elif r < 0 and s[-1] > 0:
                destroyed = False
                while s and s[-1] > 0 and s[-1] <= r * (-1):
                    if s.pop() == r * (-1):
                        destroyed = True
                        break
                if not destroyed and (not s or s[-1] < 0):
                    s.append(r)
            else:
                s.append(r)
        return s
