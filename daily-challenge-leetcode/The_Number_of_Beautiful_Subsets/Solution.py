class Solution:

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        idx_nr = defaultdict(list)

        for i, nr in enumerate(nums):
            idx_nr[nr].append(i)

        def backtrack(i, seen):
            if i > n - 1:
                return int(seen > 0)

            forbiden_present = subset_count = 0
            for j in idx_nr[nums[i] - k]:
                forbiden_present |= (1 << (j + 1)) & seen

            if not forbiden_present:
                subset_count += backtrack(i + 1, seen | (1 << (i + 1)))

            subset_count += backtrack(i + 1, seen)
            return subset_count

        return backtrack(0, 0)
