class UnionFind:
    def __init__(self, size):
        self.elm = [i for i in range(size + 1)]
        self.rank = [0] * size

    def union(self, x, y):
        xi, yi = self.find(x), self.find(y)
        if xi != yi:
            if self.rank[xi] > self.rank[yi]:
                self.elm[xi] = yi
            elif self.rank[xi] < self.rank[yi]:
                self.elm[yi] = xi
            else:
                self.elm[yi] = xi
                self.rank[xi] += 1

    def find(self, x):
        if self.elm[x] == x:
            return x
        self.elm[x] = self.find(self.elm[x])
        return self.elm[x]


class Solution:
    def areSentencesSimilarTwo(self, sentence1, sentence2, similarPairs):
        if len(sentence1) != len(sentence2):
            return False

        get_similar_i = {}
        i = 0
        for _, (x, y) in enumerate(similarPairs):
            if x not in get_similar_i:
                get_similar_i[x] = i
                i += 1
            if y not in get_similar_i:
                get_similar_i[y] = i
                i += 1
        size = len(get_similar_i)
        u = UnionFind(size)
        for _, (x, y) in enumerate(similarPairs):
            u.union(get_similar_i[x], get_similar_i[y])

        for _, (s_one, s_two) in enumerate(zip(sentence1, sentence2)):
            if s_one == s_two:
                continue
            if s_one not in get_similar_i or s_two not in get_similar_i:
                return False
            if u.find(get_similar_i[s_one]) != u.find(get_similar_i[s_two]):
                return False
        return True
