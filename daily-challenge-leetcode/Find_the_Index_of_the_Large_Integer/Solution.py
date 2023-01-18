# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:


class Solution:

    def getIndex(self, reader: 'ArrayReader') -> int:
        n = reader.length()
        left = 0
        right = n - 1

        while left < right:
            mid = (left + right) // 2
            length_left = mid - left + 1
            length_right = right - mid

            #even
            if length_left == length_right:
                o = reader.compareSub(left, mid, mid + 1, right)
                if o == 1:
                    right = mid
                else:
                    left = mid + 1
            #odd
            else:
                o = reader.compareSub(left, mid - 1, mid + 1, right)
                if o == 1:
                    right = mid - 1
                elif o == 0:
                    return mid
                else:
                    left = mid + 1
        return left
