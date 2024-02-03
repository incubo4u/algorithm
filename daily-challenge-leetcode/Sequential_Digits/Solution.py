class Solution:

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nrs = "123456789"
        start_len = len(str(low))
        end_len = len(str(high))
        ans = []
        for length in range(start_len, end_len + 1):
            for i in range(10 - length):
                if low <= (slice_nr := int(nrs[i:i + length])) <= high:
                    ans.append(slice_nr)
        return ans
