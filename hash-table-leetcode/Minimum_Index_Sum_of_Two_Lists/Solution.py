from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        one = {r:i for i , r in enumerate(list1)}
        two = {r:i for i , r in enumerate(list2)}
        choise = set(list1)  & set(list2)
        s = float("infinity")
        ret = []
        for c in choise:
            if s == one[c]+two[c]:
                ret.append(c)
            else:
                s = min(one[c]+two[c],s)
                if s == one[c]+two[c]:
                    ret = [c]
        return ret