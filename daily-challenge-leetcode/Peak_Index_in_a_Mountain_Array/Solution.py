class Solution:

    def peakIndexInMountainArray(self, arr) -> int:
        l, r, last = 0, len(arr) - 1, arr[0]
        while l < r:
            mid = (l + r) // 2
            if arr[mid] > last and arr[max(mid - 1, 0)] < arr[mid]:
                l = mid + 1
                last = arr[mid]
            else:
                r = mid
        return l - 1
