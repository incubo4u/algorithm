class Solution:

    def buildArray(self, target: List[int], n: int) -> List[str]:
        end = target[-1]
        s = 0
        ans = []
        target = set(target)
        for _ in range(end):
            s += 1
            ans.append("Push")
            if s not in target:
                ans.append("Pop")
        return ans
