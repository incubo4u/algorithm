from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if len(digits) == 0:
            return []
        button = {'2': 'abc', '3': 'def',
                  '4': 'ghi', '5': 'jkl',
                  '6': 'mno', '7': 'pqr',
                  '8': 'tuv', '9': 'wxyz'}

        def backtrack(i, comb):
            if len(comb) == len(digits):
                result.append(comb)
                return
            for d in range(len(button[digits[i]])):
                if i in range(len(digits)):
                    comb += button[digits[i]][d]
                    backtrack(i+1, comb)
                    comb = comb[:len(comb)-1]

        backtrack(0, '')
        return result
