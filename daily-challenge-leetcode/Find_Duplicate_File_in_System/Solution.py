from collections import defaultdict
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_group = defaultdict(list)
        for _, directory in enumerate(paths):
            files = directory.split(" ")
            path = files.pop(0)
            if path[-1] != "/":
                path += "/"
            for _, (f, content) in enumerate(map(lambda f: f.split("("), files)):
                content_group[content].append(path + f)
        return [group for group in content_group.values() if len(group) > 1]
