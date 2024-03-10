class Solution:

    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        for i, n in enumerate(nums):
            if not arr1 and not i % 2:
                arr1.append(n)
            elif not arr2 and i % 2:
                arr2.append(n)
            elif arr1[-1] > arr2[-1]:
                arr1.append(n)
            else:
                arr2.append(n)
        return arr1 + arr2
