# Runtime Percentile: 55.060699999999976
# Memory Percentile: 68.0162


class Solution:

    def nearestPalindromic(self, n: str) -> str:
        if len(n) == 1:
            return str(int(n) - 1)

        def my_rank(a, b):
            b = str(int(b))
            if a == b or b[::-1] != b:
                return (inf, inf)
            return abs(int(a) - int(b)), int(b)

        mid = len(n) // 2
        half = n[:mid]
        half_minus_one = str(int(half) - 1)
        half_plus_one = str(int(half) + 1)
        mid_minus_one = str(max(int(n[mid]) - 1, 0))
        mid_plus_one = str(min(int(n[mid]) + 1, 9))
        reflect_first_half = "".join((half, half[::-1]))
        reflect_first_half_if_odd = "".join((half, n[mid], half[::-1]))
        reflect_first_half_minus_one = "".join(
            (half_minus_one, half_minus_one[::-1]))
        reflect_first_half_minus_one_if_odd = "".join(
            (half_minus_one, n[mid], half_minus_one[::-1]))
        reflect_first_half_center_minus_one_if_odd = "".join(
            (half, mid_minus_one, half[::-1]))
        reflect_first_half_center_plus_one_if_odd = "".join(
            (half, mid_plus_one, half[::-1]))
        reflect_first_half_plus_one = "".join(
            (half_plus_one, half_plus_one[::-1]))
        reflect_first_half_plus_one_if_odd = "".join(
            (half_plus_one, n[mid], half_plus_one[::-1]))
        nearest_nine_only = (len(n) - 1) * "9"
        nearest_one_o_one = "1" + "0" * (len(n) - 1) + "1"

        return min(*string.digits,
                   nearest_one_o_one,
                   nearest_nine_only,
                   reflect_first_half_plus_one,
                   reflect_first_half_minus_one,
                   reflect_first_half,
                   reflect_first_half_plus_one_if_odd,
                   reflect_first_half_minus_one_if_odd,
                   reflect_first_half_center_minus_one_if_odd,
                   reflect_first_half_center_plus_one_if_odd,
                   reflect_first_half_if_odd,
                   key=lambda nr: my_rank(n, nr))
        # lol why
