from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        while data:
            info = bin(data.pop(0))[2:].zfill(8)
            if info[0] == "0":
                continue
            for o, ones in enumerate(info):
                if ones != "1":
                    break
            if  o > 4 or o <= 1:
                return False
            else:
                o -= 1
            for _ in range(o):
                if data:
                    repr = bin(data.pop(0))[2:].zfill(8)
                else:
                    return False
                if repr[:2] != "10":
                    return False
        return True
