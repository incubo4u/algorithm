# Runtime Percentile: 93.79450000000006
# Memory Percentile: 36.75430000000001


class Solution:

    def minimumPushes(self, word: str) -> int:
        keys = 8
        total = key_press_cost = 0
        for i, (_, count_char) in enumerate(Counter(word).most_common()):
            key_press_cost += int(not i % keys)
            total += count_char * key_press_cost
        return total
