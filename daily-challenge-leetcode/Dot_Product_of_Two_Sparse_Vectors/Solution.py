from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.nonzero = set( i for i, nr in enumerate(nums) if nr != 0)
        
                
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        bothnonzero = self.nonzero & vec.nonzero
        ret = 0
        if len(bothnonzero) == 0:
            return 0
        for i in bothnonzero:
            ret += self.nums[i]*vec.nums[i]
        return ret
            
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)