from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        lenght = len(flowerbed)
        for i, bed in enumerate(flowerbed):
            suitable = (i - 1 < 0 or not flowerbed[i-1]) and  (i + 1 > lenght-1 or not flowerbed[i+1])
            if suitable and not flowerbed[i]:
                flowerbed[i] = 1 
                n-=1
        return  n <= 0 
