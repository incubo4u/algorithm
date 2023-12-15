class Solution:

    def destCity(self, paths: list[list[str]]) -> str:
        f, t = zip(*paths)
        return next(iter(set(t) - set(f)))
