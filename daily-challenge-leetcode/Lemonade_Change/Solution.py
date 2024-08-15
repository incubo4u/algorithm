# Runtime Percentile: 33.34340000000003
# Memory Percentile: 68.03459999999998


class Solution:

    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = twenty = 0
        for s in bills:
            give = s
            give -= 5
            if give == 15:
                if ten:
                    ten -= 1
                elif five > 1:
                    five -= 2
                else:
                    return
                give -= 10

            if give == 5:
                if not five:
                    return
                five -= 1
                give -= 5

            twenty += s == 20
            ten += s == 10
            five += s == 5

        return 1
