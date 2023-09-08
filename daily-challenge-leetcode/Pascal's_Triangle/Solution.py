from typing import List


class Solution:

    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            n = len(ans[i - 1])
            ans.append([
                ans[-1][i - 1] + ans[-1][i] if i and i < n else 1
                for i in range(n + 1)
            ])
        return ans


# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         ret = [[1]]
#         def gen(floor,lenght):
#             if lenght > numRows:
#                 return
#             nextFloor = []
#             for i in range(lenght):
#                 left = floor[i-1] if i-1 >= 0 else 0
#                 right = floor[i] if i <= len(floor)-1 else 0
#                 sum = left+right
#                 nextFloor.append(sum)
#             ret.append(nextFloor)
#             gen(nextFloor,lenght+1)
#         gen([1],2)
#         return ret
# slower
# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         ret = [[1]]
#         for j in range(numRows-1):
#             nextFloor = []
#             floor = ret[j]
#             for i in range(j+2):
#                 left = floor[i-1] if i-1 >= 0 else 0
#                 right = floor[i] if i <= len(floor)-1 else 0
#                 sum = left+right
#                 nextFloor.append(sum)
#             ret.append(nextFloor)
#         return ret
