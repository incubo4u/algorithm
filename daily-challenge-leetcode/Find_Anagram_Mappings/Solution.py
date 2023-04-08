class Solution:

    def anagramMappings(self, nums1, nums2):
        indexes = {nr: i for i, nr in enumerate(nums2)}
        return (indexes[nr] for i, nr in enumerate(nums1))