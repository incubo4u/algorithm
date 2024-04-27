class Solution:

    def findRotateSteps(self, ring: str, key: str) -> int:
        length = len(ring)
        get_idx = defaultdict(list)
        for i, c in enumerate(ring):
            get_idx[c].append(i)

        @cache
        def unlock(r, k):
            if k > len(key) - 1:
                return 0
            ans = inf
            for i in get_idx[key[k]]:
                rotate_left = r + length - i
                rotate_right = length - r + i
                rotate_no_modulo = abs(r - i)
                rotate_cost = min(rotate_no_modulo, rotate_left, rotate_right)
                ans = min(unlock(i, k + 1) + rotate_cost + 1, ans)
            return ans

        return unlock(0, 0)
