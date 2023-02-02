from collections import defaultdict


class Solution:

    def areSentencesSimilar(self, sentence1, sentence2, similarPairs) -> bool:
        if len(sentence1) != len(sentence2):
            return
        similar = defaultdict(set)
        for a, b in similarPairs:
            similar[a].add(b)
            similar[b].add(a)

        for _, (a, b) in enumerate(zip(sentence1, sentence2)):
            if a == b or a in similar and b in similar[a]:
                continue
            break
        else:
            return True
