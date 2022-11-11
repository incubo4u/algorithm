class Solution:
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        p_lenght = len(potions)

        def bin_search(s):
            l, r = 0, p_lenght - 1

            while l < r:
                mid = (l + r) // 2
                if potions[mid] * s >= success:
                    r = mid
                else:
                    l = mid + 1

            if l == p_lenght - 1 and s * potions[l] < success:
                return 0
            else:
                return p_lenght - l

        ans = []
        for s in spells:
            ans.append(bin_search(s))
        return ans
