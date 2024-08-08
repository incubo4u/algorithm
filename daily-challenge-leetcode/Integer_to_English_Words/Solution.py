# Runtime Percentile: 91.7519
# Memory Percentile: 7.770900000000019


class Solution:

    def numberToWords(self, num: int) -> str:
        d = {
            0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
            100: "Hundred",
            1000: "Thousand",
            1000_000: "Million",
            1000_000_000: "Billion",
        }

        @cache
        def get_word(num):
            if num < 20:
                return d[num]

            if num < 100:
                res, rem = divmod(num, 10)
                suffix = get_word(rem) if rem else ""
                prefix = d[res * 10]
                return prefix + " " + suffix if suffix else prefix

            if num < 1000:
                res, rem = divmod(num, 100)
                prefix = get_word(res) + " " + d[100]
                suffix = get_word(rem) if rem else ""
                return prefix + " " + suffix if suffix else prefix

            if num < 1000_000:
                res, rem = divmod(num, 1000)
                suffix = get_word(rem) if rem else ""
                prefix = get_word(res) + " " + d[1000]
                return prefix + " " + suffix if suffix else prefix

            if num < 1000_000_000:
                res, rem = divmod(num, 1000_000)
                suffix = get_word(rem) if rem else ""
                prefix = get_word(res) + " " + d[1000_000]
                return prefix + " " + suffix if suffix else prefix

            if num >= 1000_000_000:
                res, rem = divmod(num, 1000_000_000)
                suffix = get_word(rem) if rem else ""
                prefix = get_word(res) + " " + d[1000_000_000]
                return prefix + " " + suffix if suffix else prefix

        return get_word(num)
