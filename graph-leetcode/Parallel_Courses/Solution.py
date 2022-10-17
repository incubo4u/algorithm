from collections import defaultdict, deque
from typing import List


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        g = defaultdict(list)
        indegree = defaultdict(int)
        courses = set(range(1, n + 1))
        for _, (prev_course, next_course) in enumerate(relations):
            g[prev_course].append(next_course)
            indegree[next_course] += 1
        que = deque()
        free = courses - set(indegree.keys())
        if not free:
            return -1
        semesters = 0
        que.extend(free)
        while que:
            que_lenght = len(que)
            semesters += 1
            for _ in range(que_lenght):
                course = que.popleft()
                courses.remove(course)
                for next_course in g[course]:
                    indegree[next_course] -= 1
                    if indegree[next_course] < 1:
                        que.append(next_course)
        if not courses:
            return semesters
        return -1
