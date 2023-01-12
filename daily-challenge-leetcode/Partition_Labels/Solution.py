class Solution:

    def partitionLabels(self, s: str):
        d = {char: i for i, char in enumerate(s)}
        j = start = 0
        ans = []
        for i, char in enumerate(s):
            j = max(j, d[char])
            if i == j:
                ans.append(i - start + 1)
                start = i + 1
        return ans