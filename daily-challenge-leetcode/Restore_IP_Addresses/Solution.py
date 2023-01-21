class Solution:

    def restoreIpAddresses(self, s: str):
        ans = []

        def backtrack(i, dots, s):
            if i > len(s) - 1:
                return
            if dots == 3:
                if (int_seg := int(s[i:])) >= 0 and s[i] == '0' and len(s[i:]) > 1:
                    return
                elif int_seg > 255:
                    return 
                elif len(s[i:]) < 4:
                    ans.append(s)
                return

            for j in range(i + 1, i + 4):
                if (int_seg := int(s[i:j])) > 255:
                    break
                elif len(s[i:j]) > 1 and s[i] == '0' and int(s[i:j]) >= 0:
                    break
                backtrack(j + 1, dots + 1, s[:j] + '.' + s[j:])

        backtrack(0, 0, s)
        return ans
