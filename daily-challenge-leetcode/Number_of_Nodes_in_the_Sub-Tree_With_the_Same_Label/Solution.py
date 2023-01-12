from collections import defaultdict


class Solution:

    def countSubTrees(self, n: int, edges, labels: str):
        ans = [0] * n
        g = defaultdict(list)
        for v, u in edges:
            g[u].append(v)
            g[v].append(u)

        def traverse(node=0, prev=0):
            curr = [0] * 26
            key = ord(labels[node]) - 97
            for v in g[node]:
                if v == prev:
                    continue
                bottom = traverse(v, node)
                for i in range(26):
                    curr[i] += bottom[i]
            curr[key] += 1
            ans[node] += curr[key]
            return curr

        traverse()
        return ans
