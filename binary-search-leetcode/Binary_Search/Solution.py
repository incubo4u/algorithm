def search(self, nums, target):
    mid = len(nums) // 2
    current = nums[mid]
    if current == target:
        return mid
    if mid == 0:
        return -1
    if current < target:
        return self.search(nums[mid:], target)
    if current > target:
        return self.search(nums[:mid], target)

def search_iter(self, nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        current = nums[mid]
        if current == target:
            return mid
        if current > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1
