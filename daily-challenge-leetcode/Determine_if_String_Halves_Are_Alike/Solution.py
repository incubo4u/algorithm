class Solution:

    def halvesAreAlike(self, s: str) -> bool:
        seen = {
            'a': 0,
            'e': 0,
            'i': 0,
            'o': 0,
            'u': 0,
        }
        mid = ((len(s) - 1) // 2)
        for c in s[:mid + 1]:
            if c.lower() in seen:
                seen[c.lower()] += 1
        for c in s[mid + 1:]:
            if c.lower() in seen:
                seen[c.lower()] -= 1
        return sum(seen.values()) == 0
