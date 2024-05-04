class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        v1, v2 = v1.split("."), v2.split(".")
        for k, (c, cc) in enumerate(zip(v1, v2)):
            i, ii = int(c), int(cc)
            if i > ii:
                return 1
            if i < ii:
                return -1

        if v1_is_v2 := len(v1) < len(v2):
            v1 = v2

        for c in v1[min(k + 1, len(v1)) :]:
            if int(c):
                return -1 if v1_is_v2 else 1

        return 0
