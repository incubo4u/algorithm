class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        longer, shorter = num1[::-1], num2[::-1]
        if len(shorter) > len(longer):
            longer, shorter = longer, shorter

        def get_partial(longer, shorter):
            partials = []
            for i, d1 in enumerate(shorter):
                carry = 0
                d1 = ord(d1) - ord('0')
                partial = []
                for d2 in longer:
                    d2 = ord(d2) - ord('0')
                    partial.append((mul := d1 * d2 + carry) % 10)
                    carry = mul // 10
                if carry:
                    partial.append(carry)
                partials.append(([0] * i) + partial)
            return partials

        def align(partials):
            lenght = len(max(partials, key=len))
            for p in partials:
                fill = lenght - len(p)
                p += [0] * fill
            return partials

        def add(partials):
            partials = align(partials)
            s = []
            carry = 0
            for j in range(len(partials[0])):
                d = 0
                for i in range(len(partials)):
                    d += partials[i][j]
                s.append(str((d + carry) % 10))
                carry = (d + carry) // 10
            if carry:
                s.append(str(carry))
            return s

        ans = add((get_partial(longer, shorter)))
        if '0' in (sans := set(ans)) and len(sans) == 1:
            return '0'
        return ''.join(ans[::-1])
