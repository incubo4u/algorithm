from collections import defaultdict


class ValidWordAbbr:
    def __init__(self, dictionary):
        self.d = defaultdict(set)
        for _, (key, value) in enumerate(map(lambda s: (s[0] + str(len(s) - 2) + s[len(s) - 1], s), dictionary)):
            self.d[key].add(value)

    def isUnique(self, word: str) -> bool:
        abr = word[0] + str(len(word) - 2) + word[len(word) - 1]
        if abr not in self.d:
            return True
        return word in self.d[abr] and len(self.d[abr]) < 2
