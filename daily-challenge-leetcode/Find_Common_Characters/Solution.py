from collections import Counter
from functools import reduce


class Solution:

    def commonChars(self, words):
        return reduce(lambda c, cc: c & cc, map(Counter, words)).elements()
