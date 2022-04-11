def search(self, nums, target):
    i = len(nums) // 2
    current = nums[i]
    if current == target:
        return i
    if i == 0:
        return -1
    if current < target:
        return self.search(nums[i:], target)
    if current > target:
        return self.search(nums[:i], target)

def search_iter(self, nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        i = left + (right - left) // 2
        current = nums[i]
        if current == target:
            return i
        if current > target:
            right = i - 1
        else:
            left = i + 1
    return -1
