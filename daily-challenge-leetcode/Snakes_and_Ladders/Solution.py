class Solution:

    def snakesAndLadders(self, board):
        n = len(board)
        flat = []
        for i in range(n):
            if i % 2:
                flat.extend(board.pop()[::-1])
            else:
                flat.extend(board.pop())

        seen = [None] * (n * n)
        seen[0] = 0
        que = deque()
        que.append(0)

        while que:
            curr = que.popleft()
            for die in range(1, 7):
                next_cell = curr + die

                if flat[next_cell] != -1:
                    next_cell = flat[next_cell] - 1

                if next_cell == n * n - 1:
                    return seen[curr] + 1

                if seen[next_cell] is None:
                    que.append(next_cell)
                    seen[next_cell] = seen[curr] + 1
        return -1
