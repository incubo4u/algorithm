from math import ceil


class Solution:

    def minimumTime(self, jobs: list[int], workers: list[int]) -> int:
        days = 0
        for _, (w, j) in enumerate(zip(sorted(workers), sorted(jobs))):
            days = max(ceil(j / w), days)
        return days
