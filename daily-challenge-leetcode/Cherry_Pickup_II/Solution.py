from typing import List
from math import inf
from functools import cache


class Solution:

    def cherryPickup(self, g: List[List[int]]) -> int:
        end = len(g)
        row_length = len(g[0])

        @cache
        def traverse(i, robot_one, robot_two):
            if robot_one < 0 or robot_two < 0:
                return -inf
            if robot_one > row_length - 1 or robot_two > row_length - 1:
                return -inf
            if i == end:
                return 0

            return max(
                traverse(i + 1, robot_one + 1, robot_two + 1),  # one r two r  
                traverse(i + 1, robot_one - 1, robot_two - 1),  # one l two l 
                traverse(i + 1, robot_one + 1, robot_two - 1),  # one r two l 
                traverse(i + 1, robot_one - 1, robot_two + 1),  # one l two r
                traverse(i + 1, robot_one, robot_two + 1),      # one - two r
                traverse(i + 1, robot_one, robot_two - 1),      # one - two l
                traverse(i + 1, robot_one, robot_two),          # one - two - 
                traverse(i + 1, robot_one + 1, robot_two),      # one r two - 
                traverse(i + 1, robot_one - 1, robot_two),      # one l two - 
            ) + ((g[i][robot_one] + g[i][robot_two]) *
                 int(robot_one != robot_two)) + (g[i][robot_one] *
                                                 int(robot_one == robot_two))

        return traverse(0, 0, row_length - 1)
