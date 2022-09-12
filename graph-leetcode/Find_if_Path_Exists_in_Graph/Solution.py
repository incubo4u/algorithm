from collections import defaultdict
from typing import List


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        neighbours = defaultdict(list)
        seen = set()
        for _, (start, end) in enumerate(edges):
            neighbours[start].append(end)
            neighbours[end].append(start)
        stack = [source]
        while stack:
            node = stack.pop()
            seen.add(node)
            if node == destination:
                return True
            for _, n in enumerate(neighbours[node]):
                if n in seen:
                    continue
                stack.append(n)
        return False
