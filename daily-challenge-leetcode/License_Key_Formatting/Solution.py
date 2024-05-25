class Solution:

    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = "".join([chunk.upper() for chunk in s.split("-")])
        n = len(s)
        overflow = n % k
        ans = []
        if overflow:
            ans.append(s[:overflow])
        ans += [s[i:i + k] for i in range(overflow, n, k)]
        return "-".join(ans)
