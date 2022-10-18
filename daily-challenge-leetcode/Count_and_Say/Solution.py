from collections import deque


class Solution:
    def countAndSay(self, n: int) -> str:
        def generate(prev_seq=deque("1"), times=1):
            if times == n:
                return "".join(prev_seq)
            last = prev_seq[0]
            count = 0
            curr_seq = deque()
            for _ in range(len(prev_seq)):
                if prev_seq[0] == last:
                    count += 1
                else:
                    curr_seq.append(str(count))
                    curr_seq.append(last)
                    count = 1
                last = prev_seq.popleft()
            if not curr_seq or curr_seq[-1] != last:
                curr_seq.append(str(count))
                curr_seq.append(last)
            return generate(curr_seq, times + 1)

        return generate()
