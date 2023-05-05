class Solution:

    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        que = deque('0123456789')
        limit = len(str(high))
        ans = set()
        while que:
            curr = que.popleft()
            if len(curr) > limit or (nr := int(curr)) > high:
                continue
            if nr >= low:
                ans.add(nr)
            last_c = curr[-1]
            if last_c == '9':
                que.append(curr + '8')
            elif last_c == '0':
                que.append(curr + '1')
            else:
                que.append(curr + chr(ord(last_c) + 1))
                que.append(curr + chr(ord(last_c) - 1))
        return sorted(ans)